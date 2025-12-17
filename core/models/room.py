from datetime import datetime
from typing import Optional

from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Room(Base):
    name: Mapped[str] = mapped_column(String)

    user_id: Mapped[Optional[int]] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=True,
        unique=True,
    )

    user: Mapped[Optional["User"]] = relationship(
        "User", back_populates="room", uselist=False
    )

    book_start: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    book_end: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    status: Mapped[bool] = mapped_column(Boolean)
