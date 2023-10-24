__all__ = ["router"]

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/currency", tags=["Currency"])

import src.api.currency.routes  # noqa: E402, F401
