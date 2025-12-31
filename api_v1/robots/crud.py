from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Robot
from . import schemas


async def get_all_robots(session: AsyncSession) -> list[Robot]:
    stmt = select(Robot).order_by(Robot.id)
    result: Result = await session.execute(stmt)
    robots = result.scalars().all()
    return list(robots)


async def get_robot(session: AsyncSession, robot_id) -> Robot | None:
    return await session.get(Robot, robot_id)
