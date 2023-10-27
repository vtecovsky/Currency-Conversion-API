from abc import ABC, abstractmethod


class AbstractCurrencyRepository(ABC):
    @abstractmethod
    async def run_update_exchange_rates(self) -> None:
        ...

    @abstractmethod
    async def update_exchange_rates(self, rates: dict) -> None:
        ...

    @abstractmethod
    async def get_last_update_time(self):
        ...

    @abstractmethod
    async def setup_update_time(self, timestamp) -> None:
        ...

    @abstractmethod
    async def convert_currency(self, from_currency: str, target_currency: str, amount: float) -> float:
        ...
