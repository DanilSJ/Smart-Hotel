from typing import Optional

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Robot(Base):
    name: Mapped[str] = mapped_column(String)

    deliver: Mapped[bool] = mapped_column(Boolean, default=False)
    deliver_status: Mapped[str] = mapped_column(String, nullable=True)
    deliver_room: Mapped[Optional["Room"]] = relationship(
        "Room", back_populates="robot"
    )

    status: Mapped[str] = mapped_column(String)
