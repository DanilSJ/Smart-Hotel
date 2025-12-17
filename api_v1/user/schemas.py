from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    name: str

    phone: int

    room: Optional[int] = None

    start_life: Optional[datetime] = None
    end_life: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class RegisterSchema(BaseModel):
    name: str
    password: bytes
    phone: int

    model_config = ConfigDict(from_attributes=True)
