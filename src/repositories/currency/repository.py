from datetime import datetime

from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

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

    async def setup_update(self) -> None:
        async with self._create_session() as session:
            now_datetime = datetime.now()
            if await self.get_last_update() is not None:
                query = (
                    update(LastCurrencyUpdate.updated_at).values(updated_at=now_datetime).returning(LastCurrencyUpdate)
                )
            else:
                query = insert(LastCurrencyUpdate).values(updated_at=now_datetime).returning(LastCurrencyUpdate)
            await session.scalar(query)
            await session.commit()
