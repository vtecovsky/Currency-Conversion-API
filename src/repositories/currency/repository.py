import json

import aiohttp
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import settings
from src.repositories.currency.abc import AbstractCurrencyRepository
from src.storage.sql import AbstractSQLAlchemyStorage
from src.storage.sql.models import Currency, LastCurrencyUpdate


class SqlCurrencyRepository(AbstractCurrencyRepository):
    storage: AbstractSQLAlchemyStorage

    def __init__(self, storage: AbstractSQLAlchemyStorage):
        self.storage = storage

    def _create_session(self) -> AsyncSession:
        return self.storage.create_session()

    async def get_last_update(self):
        async with self._create_session() as session:
            query = select(LastCurrencyUpdate.updated_at)
            selected_obj = await session.scalar(query)
            return selected_obj

    async def setup_update_time(self, timestamp) -> None:
        async with self._create_session() as session:
            if await self.get_last_update() is not None:
                query = (
                    update(LastCurrencyUpdate).values(updated_at=timestamp).returning(LastCurrencyUpdate)
                )
            else:
                query = insert(LastCurrencyUpdate).values(updated_at=timestamp).returning(LastCurrencyUpdate)
            await session.scalar(query)
            await session.commit()

    async def update_currency_rates(self) -> None:
        async with (aiohttp.ClientSession() as session):
            url = "http://api.exchangeratesapi.io/v1/latest"
            params = {"access_key": settings.ACCESS_KEY}
            async with session.get(url, params=params) as response:
                response_text = await response.text()
                response_json = json.loads(response_text)
                timestamp = response_json.get("timestamp")
                await self.setup_update_time(timestamp)
                return response_json

    async def convert_currency(self, from_currency: str, to_currency: str, amount: float) -> float:
        await self.update_currency_rates()