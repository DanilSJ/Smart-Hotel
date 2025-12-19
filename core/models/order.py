from typing import Optional

from sqlalchemy import Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Order(Base):
    manu_id: Mapped[Optional[int]] = mapped_column(
        Integer,
        ForeignKey("menus.id"),
        nullable=True,
        unique=True,
    )

    menu: Mapped[Optional["Menu"]] = relationship(
        "Menu", back_populates="order", uselist=False
    )
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
