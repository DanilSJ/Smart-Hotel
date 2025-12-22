from pydantic import BaseModel, ConfigDict


class RoomSchema(BaseModel):

    model_config = ConfigDict(from_attributes=True)
