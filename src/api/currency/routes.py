import aiohttp

from src.api.currency import router
from src.api.dependencies import CURRENCY_REPOSITORY_DEPENDENCY
from src.config import settings


@router.get("/exchange_rates")
async def get_exchange_rates(currency_repository: CURRENCY_REPOSITORY_DEPENDENCY):
    async with (aiohttp.ClientSession() as session):
        url = "http://api.exchangeratesapi.io/v1/latest"
        params = {"access_key": settings.ACCESS_KEY}
        async with session.get(url, params=params) as response:
            response_text = await response.text()
            await currency_repository.setup_update()
            print(response_text)

    # TODO Использовать внешний апи, чтобы получить информацию о валютах
    #  Сохранить обновленные данные в базу данных, добавить запись об обновлении.


@router.get("/last_update")
async def get_last_currency_update(currency_repository: CURRENCY_REPOSITORY_DEPENDENCY):
    # TODO Обработать случай, когда не было еще обновления в БД.
    last_update = await currency_repository.get_last_update()
    return last_update.strftime('%Y-%m-%d %H:%M:%S')


@router.get("/convert")
async def convert_currency():
    # TODO Принимает на вход 2 валюты, нужно получить сначала
    #  актуальный курс, затем произвести конвертацию.
    ...
