from src.api.currency import router


@router.get("/update_currency_rates")
async def update_currency_rates():
    # TODO Использовать внешний апи, чтобы получить информацию о валютах
    ...


@router.get("/last_currency_update")
async def last_currency_update():
    # TODO Возвращать время последнего изменения
    ...


@router.get("/currency_convert")
async def currency_convert():
    # TODO Принимает на вход 2 валюты, нужно получить сначала
    #  актуальный курс, затем произвести конвертацию.
    ...
