from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.currency.abc import AbstractCurrencyRepository
from src.storage.sql import AbstractSQLAlchemyStorage


class SqlCurrencyRepository(AbstractCurrencyRepository):
    storage: AbstractSQLAlchemyStorage

    def __init__(self, storage: AbstractSQLAlchemyStorage):
        self.storage = storage

    def _create_session(self) -> AsyncSession:
        return self.storage.create_session()
