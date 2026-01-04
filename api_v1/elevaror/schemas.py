from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ElevatorSchema(BaseModel):
    id: int
    floor_id: str
    status: str

    model_config = ConfigDict(from_attributes=True)
