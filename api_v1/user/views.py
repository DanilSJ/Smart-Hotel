from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from .schemas import UserSchema
from . import crud

router = APIRouter()

@router.get("/{user_id}/", response_model=UserSchema)
async def get_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    result = await crud.get_user(session, user_id)
    if not result:
        raise HTTPException(status_code=404)

    return result

