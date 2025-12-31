from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core.models import db_helper
from . import schemas
from . import crud
from api_v1.auth.views import get_token, get_current_user
from api_v1.user.crud import get_user
from ..utils import check_administrator

router = APIRouter()


@router.get("/", response_model=list[schemas.RoomSchema])
async def get_all_rooms(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_all_rooms(session)


@router.get("/{id}/", response_model=schemas.RoomSchema)
async def get_room(
    room_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_room(session, room_id)


@router.put("/book/", response_model=schemas.RoomSchema)
async def book_room(
    data: schemas.RoomBookSchema,
    token: str = Depends(get_token),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user_id = await get_current_user(token)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    await check_administrator(session, user_id)

    return await crud.book_room(
        session, data.id, data.book_start, data.book_end, data.user_id
    )


@router.get("/{room_id}/availability/", response_model=schemas.RoomSchema)
async def get_room_availability(
    room_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_room_availability(session, room_id)
