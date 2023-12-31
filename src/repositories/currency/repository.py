import json

import aiohttp
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import settings
from src.exceptions import (CurrencyNotFound, ErrorFromExternalAPI,
                            NegativeAmountOfMoney)
from src.repositories.currency.abc import AbstractCurrencyRepository
from src.storage.sql import AbstractSQLAlchemyStorage
from src.storage.sql.models import Currency, LastCurrencyUpdate


class SqlCurrencyRepository(AbstractCurrencyRepository):
    storage: AbstractSQLAlchemyStorage

    def __init__(self, storage: AbstractSQLAlchemyStorage):
        self.storage = storage

    def _create_session(self) -> AsyncSession:
        return self.storage.create_session()

    async def get_last_update_time(self):
        async with self._create_session() as session:
            query = select(LastCurrencyUpdate.updated_at)
            selected_obj = await session.scalar(query)
            return selected_obj

    async def setup_update_time(self, timestamp) -> None:
        async with self._create_session() as session:
            if await self.get_last_update_time() is not None:
                query = update(LastCurrencyUpdate).values(updated_at=timestamp).returning(LastCurrencyUpdate)
            else:
                query = insert(LastCurrencyUpdate).values(updated_at=timestamp).returning(LastCurrencyUpdate)
            await session.scalar(query)
            await session.commit()

    @staticmethod
    async def get_response_from_api() -> json:
        async with (aiohttp.ClientSession() as session):
            url = "http://api.exchangeratesapi.io/v1/latest"
            params = {"access_key": settings.ACCESS_KEY}
            async with session.get(url, params=params) as response:
                response_text = await response.text()
                response_json = json.loads(response_text)
                if not response_json.get("success"):
                    raise ErrorFromExternalAPI()
                return response_json

    async def update_exchange_rates(self, rates: dict) -> None:
        async with self._create_session() as session:
            if await self.get_last_update_time() is not None:
                for currency_code, exchange_rate in rates.items():
                    query = (
                        update(Currency)
                        .where(Currency.code == currency_code)
                        .values(rate=exchange_rate)
                        .returning(Currency)
                    )
                    await session.scalar(query)
                    await session.commit()
            else:
                from src.repositories.currency.utils import currency_dict

                for currency_code, exchange_rate in rates.items():
                    currency_name = currency_dict.get(currency_code)
                    query = (
                        insert(Currency)
                        .values(name=currency_name, code=currency_code, rate=exchange_rate)
                        .returning(Currency)
                    )
                    await session.scalar(query)
                    await session.commit()

    async def run_update_exchange_rates(self) -> None:
        response = await self.get_response_from_api()
        await self.update_exchange_rates(response.get("rates"))
        timestamp = response.get("timestamp")
        await self.setup_update_time(timestamp)

    async def convert_to_base(self, amount: float, from_currency: str) -> float:
        async with self._create_session() as session:
            query = select(Currency).where(Currency.code == from_currency)
            obj = await session.scalar(query)
            if not obj:
                raise CurrencyNotFound()
            return amount / obj.rate

    async def convert_to_target(self, amount: float, target_currency: str) -> float:
        async with self._create_session() as session:
            query = select(Currency).where(Currency.code == target_currency)
            obj = await session.scalar(query)
            if not obj:
                raise CurrencyNotFound()
            return amount * obj.rate

    async def convert_currency(self, from_currency: str, target_currency: str, amount: float) -> float:
        if amount < 0:
            raise NegativeAmountOfMoney()
        if from_currency == target_currency or amount == 0:
            return amount
        await self.run_update_exchange_rates()
        base_amount = await self.convert_to_base(amount, from_currency)
        final_amount = await self.convert_to_target(base_amount, target_currency)
        return round(final_amount, 2)
