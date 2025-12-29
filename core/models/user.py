from typing import Optional

from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class User(Base):
    name: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

    phone: Mapped[int] = mapped_column(Integer)

    room: Mapped[Optional["Room"]] = relationship(
        "Room", back_populates="user", uselist=False
    )

    admin: Mapped[bool] = mapped_column(Boolean, default=False)
