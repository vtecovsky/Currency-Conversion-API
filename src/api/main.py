from fastapi import FastAPI

from config import settings
from src.api.dependencies import Dependencies
# from src.api.routers import routers
from src.repositories.currency.repository import SqlCurrencyRepository
from src.storage.sql import PostgresSQLAlchemyStorage

app = FastAPI()


async def setup_repositories():
    storage = PostgresSQLAlchemyStorage.from_url(settings.DB_URL)
    participant_repository = SqlCurrencyRepository(storage)
    Dependencies.set_storage(storage)

    # await storage.drop_all()
    # await storage.create_all()


@app.on_event("startup")
async def startup_event():
    await setup_repositories()


# for router in routers:
#     app.include_router(router)
