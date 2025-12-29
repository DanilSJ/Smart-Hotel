from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RoomSchema(BaseModel):
    id: int
    name: str
    status: str

    model_config = ConfigDict(from_attributes=True)


class RoomBook(BaseModel):
    id: int
    status: str

    model_config = ConfigDict(from_attributes=True)


class RoomBookSchema(BaseModel):
    id: int
    book_start: datetime
    book_end: datetime
    user_id: int

    model_config = ConfigDict(from_attributes=True)
