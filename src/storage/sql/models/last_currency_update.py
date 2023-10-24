import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.storage.sql.models import Base


class Currency(Base):
    __tablename__ = "last_currency_update"
    updated_at: Mapped[datetime.datetime] = mapped_column()
