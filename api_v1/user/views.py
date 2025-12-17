from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import schemas
from . import crud

router = APIRouter()


@router.get("/{user_id}/", response_model=schemas.UserSchema)
async def get_user_by_id(
    user_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    result = await crud.get_user(session, user_id)
    if not result:
        raise HTTPException(status_code=404)

    return result


@router.post("/", response_model=schemas.UserSchema)
async def create_user(
    user_in: schemas.RegisterSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(session=session, user_in=user_in)


#
# @router.patch("/", response_model=schemas.UserSchema)
# async def update_user(
#         user_id: int,
#         user_in: schemas.UpdateSchema,
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     return await crud.update_user(session=session, user_id=user_id, user_in=user_in)
