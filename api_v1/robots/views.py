from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import schemas
from . import crud
from api_v1.auth.views import get_token, get_current_user
from api_v1.utils import check_administrator

router = APIRouter()


@router.get("/", response_model=list[schemas.RobotSchema])
async def get_all_robots(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_all_robots(session)


@router.get("/{robot_id}/", response_model=schemas.RobotSchema)
async def get_robot(
    robot_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_robot(session, robot_id)


@router.put("/{robot_id}/status", response_model=schemas.RobotSchema)
async def update_robot_status(
    robot_id: int,
    token: str = Depends(get_token),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user_id = await get_current_user(token)
    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
        )

    await check_administrator(session, user_id)

    return await crud.update_robot_status(session, robot_id)


@router.put("/{robot_id}/deliver", response_model=schemas.RobotSchema)
async def update_robot_deliver(
    robot_id: int,
    room_id: int,
    token: str = Depends(get_token),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user_id = await get_current_user(token)
    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
        )

    await check_administrator(session, user_id)

    return await crud.update_robot_deliver(session, robot_id, room_id)


@router.get("/deliveries/", response_model=list[schemas.RobotSchema])
async def get_deliveries(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_deliveries(session)


@router.get("/deliveries/{robot_id}/", response_model=schemas.RobotSchema)
async def get_delivery(
    robot_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_delivery(session, robot_id)
