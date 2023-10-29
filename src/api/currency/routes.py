import datetime

from src.api.currency import router
from src.api.dependencies import CURRENCY_REPOSITORY_DEPENDENCY
from src.exceptions import NoLastUpdate


@router.post("/exchange_rates")
async def update_exchange_rates(currency_repository: CURRENCY_REPOSITORY_DEPENDENCY) -> dict:
    await currency_repository.run_update_exchange_rates()
    return {"success": True}


@router.get("/last_update")
async def get_last_currency_update(currency_repository: CURRENCY_REPOSITORY_DEPENDENCY) -> str:
    last_update = await currency_repository.get_last_update_time()
    if not last_update:
        raise NoLastUpdate()
    dt = datetime.datetime.fromtimestamp(last_update)
    formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date


@router.get("/convert")
async def convert_currency(
        from_currency: str, target_currency: str, amount: float, currency_repository: CURRENCY_REPOSITORY_DEPENDENCY
) -> float:
    return await currency_repository.convert_currency(from_currency, target_currency, amount)
