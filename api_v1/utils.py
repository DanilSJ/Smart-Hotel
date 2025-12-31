from fastapi import HTTPException
from api_v1.user.crud import get_user
from core.models import User


async def check_administrator(session, user_id) -> User:
    user = await get_user(session, user_id)

    if not user.admin:
        raise HTTPException(status_code=401, detail="You are not an admin")

    return user
