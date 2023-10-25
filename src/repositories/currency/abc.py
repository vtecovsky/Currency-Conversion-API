from abc import ABC, abstractmethod


class AbstractCurrencyRepository(ABC):

    @abstractmethod
    async def update_currency_rates(self) -> None:
        ...

    @abstractmethod
    async def get_last_update(self):
        ...

    @abstractmethod
    async def setup_update_time(self, timestamp) -> None:
        ...

    @abstractmethod
    async def convert_currency(self, from_currency: str, to_currency: str, amount: float) -> float:
        ...
