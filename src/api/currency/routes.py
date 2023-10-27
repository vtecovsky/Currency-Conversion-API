import datetime

from src.api.currency import router
from src.api.dependencies import CURRENCY_REPOSITORY_DEPENDENCY


@router.post("/exchange_rates")
async def update_exchange_rates(currency_repository: CURRENCY_REPOSITORY_DEPENDENCY):
    res = await currency_repository.run_update_exchange_rates()
    return res
    # TODO Использовать внешний апи, чтобы получить информацию о валютах
    #  Сохранить обновленные данные в базу данных, добавить запись об обновлении.


@router.get("/last_update")
async def get_last_currency_update(currency_repository: CURRENCY_REPOSITORY_DEPENDENCY):
    # TODO Обработать случай, когда не было еще обновления в БД.
    last_update = await currency_repository.get_last_update_time()
    if last_update is not None:
        dt = datetime.datetime.fromtimestamp(last_update)
        formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_date
    return {"message": "No last update"}


@router.get("/convert")
async def convert_currency(
    from_currency: str, target_currency: str, amount: float, currency_repository: CURRENCY_REPOSITORY_DEPENDENCY
):
    # TODO Принимает на вход 2 валюты, нужно получить сначала
    #  актуальный курс, затем произвести конвертацию.
    return await currency_repository.convert_currency(from_currency, target_currency, amount)
