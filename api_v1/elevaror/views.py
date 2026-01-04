from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import schemas
from . import crud
from api_v1.auth.views import get_token, get_current_user
from api_v1.utils import check_administrator

router = APIRouter()


@router.get("/", response_model=list[schemas.ElevatorSchema])
async def get_elevators(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_elevators(session)


@router.post("/elevators/{elevator_id}/call", response_model=schemas.ElevatorSchema)
async def call_elevator(
    elevator_id: int,
    token: str = Depends(get_token),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user_id = await get_current_user(token)
    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
        )

    # Логика вызова лифта


@router.post("/elevators/{elevator_id}/move", response_model=schemas.ElevatorSchema)
async def move_elevator(
    elevator_id: int,
    token: str = Depends(get_token),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user_id = await get_current_user(token)
    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
        )

    # Логика перемещения лифта


@router.get("/elevators/{elevator_id}/status", response_model=schemas.ElevatorSchema)
async def get_elevator_status(
    elevator_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_elevator(session, elevator_id)
