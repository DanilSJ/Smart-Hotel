from datetime import datetime

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Reception(Base):
    guest: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    start: Mapped[datetime] = mapped_column(DateTime)
    end: Mapped[datetime] = mapped_column(DateTime)
