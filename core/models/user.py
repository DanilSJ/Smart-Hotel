from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class User(Base):
    name: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

    phone: Mapped[int] = mapped_column(Integer)

    room: Mapped[int] = mapped_column(Integer)

    start_life: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    end_life: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
