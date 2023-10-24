from sqlalchemy.orm import Mapped, mapped_column

from src.storage.sql.__mixin__ import IdMixin
from src.storage.sql.models import Base


class Currency(Base, IdMixin):
    __tablename__ = "currency"
    name: Mapped[str] = mapped_column(unique=True)
    code: Mapped[int] = mapped_column(unique=True)
    exchange_rate: Mapped[float] = mapped_column()
