from abc import ABC, abstractmethod


class AbstractCurrencyRepository(ABC):
    @abstractmethod
    async def get_last_update(self):
        ...

    @abstractmethod
    async def setup_update(self) -> None:
        ...
