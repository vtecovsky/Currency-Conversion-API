from src.api.currency import router as router_currency

routers = [router_currency]

__all__ = ["routers", *routers]
