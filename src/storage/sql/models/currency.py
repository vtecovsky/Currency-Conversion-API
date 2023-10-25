from sqlalchemy.orm import Mapped, mapped_column

from src.storage.sql.models import Base


class Currency(Base):
    __tablename__ = "currency"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    code: Mapped[str] = mapped_column()
    rate: Mapped[float] = mapped_column()
