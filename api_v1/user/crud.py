from fastapi import HTTPException
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import User
from . import schemas
import bcrypt



async def get_all_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)

async def get_user(session: AsyncSession, user_id) -> User | None:
    return await session.get(User, user_id)

async def create_user(session: AsyncSession, user_in: schemas.RegisterSchema) -> User:
    stmt = select(User).where(User.name == user_in.name)
    result: Result = await session.execute(stmt)

    if result.scalars().first():
        raise HTTPException(status_code=409, detail="User already exists")

    hashed = bcrypt.hashpw(user_in.password, bcrypt.gensalt())
    user_in.password = hashed

    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user
