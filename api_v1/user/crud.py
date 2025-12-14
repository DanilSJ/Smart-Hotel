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
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user
