from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    name: str

    phone: int

    model_config = ConfigDict(from_attributes=True)


class RegisterSchema(BaseModel):
    name: str
    password: bytes
    phone: int

    model_config = ConfigDict(from_attributes=True)


class LoginSchema(BaseModel):
    name: str
    password: bytes

    model_config = ConfigDict(from_attributes=True)


class UpdateSchema(BaseModel):
    id: int
    name: str
    phone: int

    model_config = ConfigDict(from_attributes=True)
