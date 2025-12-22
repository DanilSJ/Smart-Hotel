from fastapi import HTTPException
from sqlalchemy.engine import Result
from sqlalchemy.exc import StatementError
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


async def login_user(session: AsyncSession, name: str, password: bytes) -> User:
    stmt = select(User).where(User.name == name)
    result: Result = await session.execute(stmt)

    for el in result.scalars().all():
        if bcrypt.checkpw(password, el.password):
            return el

    raise HTTPException(status_code=409, detail="Incorrect password")


async def update_user(
    session: AsyncSession, user_id: int, user_in: schemas.UpdateSchema
) -> schemas.UserSchema:
    stmt = select(User).where(User.id == user_id)
    result = await session.execute(stmt)
    user = result.scalars().first()

    if user:
        try:
            for field, value in user_in.model_dump(exclude_unset=True).items():
                setattr(user, field, value)

            await session.commit()
            await session.refresh(user)

            return schemas.UserSchema.model_validate(user)
        except StatementError:
            raise HTTPException(status_code=400, detail="Incorrect arguments")

    raise HTTPException(status_code=404, detail="User does not exist")
