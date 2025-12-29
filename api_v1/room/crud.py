from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Room, User
from . import schemas


async def get_all_rooms(session: AsyncSession) -> list[Room]:
    stmt = select(Room).order_by(Room.id)
    result: Result = await session.execute(stmt)
    rooms = result.scalars().all()
    return list(rooms)


async def get_room(session: AsyncSession, room_id) -> Room | None:
    return await session.get(Room, room_id)


async def book_room(
    session: AsyncSession,
    room_id: int,
    book_start: datetime,
    book_end: datetime,
    user_id: int,
) -> Room:
    stmt = select(Room).where(Room.id == room_id)
    result = await session.execute(stmt)
    room = result.scalars().first()

    stmt_user = select(User).where(User.id == user_id)
    result_user = await session.execute(stmt_user)
    user = result_user.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    if room.status == "booked":
        raise HTTPException(status_code=400, detail="Already booked")

    room.status = "booked"
    room.book_start = book_start
    room.book_end = book_end
    room.user_id = user_id

    await session.commit()
    await session.refresh(room)
    return room
