from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core.models import db_helper
from . import schemas
from . import crud
from api_v1.auth.views import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_current_user,
    get_token,
    Token,
)

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


@router.post("/login/")
async def login_user(
    data: schemas.LoginSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user = await crud.login_user(session, data.name, data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")


@router.get("/auth/check/")
async def auth_check(token: str = Depends(get_token)):
    return await get_current_user(token)


#
# @router.patch("/", response_model=schemas.UserSchema)
# async def update_user(
#         user_id: int,
#         user_in: schemas.UpdateSchema,
#         session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     return await crud.update_user(session=session, user_id=user_id, user_in=user_in)
