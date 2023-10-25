from typing import Annotated

from fastapi import Depends

from src.repositories.currency.abc import AbstractCurrencyRepository
from src.storage.sql import AbstractSQLAlchemyStorage


class Dependencies:
    _storage: "AbstractSQLAlchemyStorage"
    _currency_repository: "AbstractCurrencyRepository"

    @classmethod
    def get_storage(cls) -> "AbstractSQLAlchemyStorage":
        return cls._storage

    @classmethod
    def set_storage(cls, storage: "AbstractSQLAlchemyStorage"):
        cls._storage = storage

    @classmethod
    def get_currency_repository(cls) -> "AbstractCurrencyRepository":
        return cls._currency_repository

    @classmethod
    def set_currency_repository(cls, currency_repository: "AbstractCurrencyRepository"):
        cls._currency_repository = currency_repository


STORAGE_DEPENDENCY = Annotated[AbstractSQLAlchemyStorage, Depends(Dependencies.get_storage)]
CURRENCY_REPOSITORY_DEPENDENCY = Annotated[AbstractCurrencyRepository, Depends(Dependencies.get_currency_repository)]
