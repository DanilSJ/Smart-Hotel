from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Elevator
from . import schemas


async def get_elevators(session: AsyncSession) -> list[Elevator]:
    stmt = select(Elevator).order_by(Elevator.id)
    result = await session.execute(stmt)
    elevators = result.scalars().all()
    return list(elevators)


async def get_elevator(session: AsyncSession, elevator_id) -> Elevator | None:
    return await session.get(Elevator, elevator_id)
