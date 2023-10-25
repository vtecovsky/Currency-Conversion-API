from sqlalchemy.orm import Mapped, mapped_column

from src.storage.sql.models import Base


class Currency(Base):
    __tablename__ = "currency"
    name: Mapped[str] = mapped_column()
    code: Mapped[str] = mapped_column(unique=True, primary_key=True)
    rate: Mapped[float] = mapped_column()
