from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Elevator(Base):
    floor_id: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String)
