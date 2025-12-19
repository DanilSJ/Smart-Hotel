from typing import Optional

from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Menu(Base):
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    exists: Mapped[bool] = mapped_column(Boolean)

    order: Mapped[Optional["Order"]] = relationship(
        "Order", back_populates="menu", uselist=False
    )
