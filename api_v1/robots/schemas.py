from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RobotSchema(BaseModel):
    id: int
    name: str
    status: str

    model_config = ConfigDict(from_attributes=True)
