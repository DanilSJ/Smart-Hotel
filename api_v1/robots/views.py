from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import schemas
from . import crud

router = APIRouter()


@router.get("/", response_model=list[schemas.RobotSchema])
async def get_all_robots(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_all_robots(session)


@router.get("/{id}/", response_model=schemas.RobotSchema)
async def get_robot(
    robot_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_robot(session, robot_id)
