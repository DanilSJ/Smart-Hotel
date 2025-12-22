from fastapi import APIRouter
from . import schemas

router = APIRouter()

@router.get("/", response_model=schemas.RoomSchema)
async def get_all_rooms():
    pass