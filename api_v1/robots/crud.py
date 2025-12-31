from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.models import Robot
from . import schemas


async def get_all_robots(session: AsyncSession) -> list[Robot]:
    stmt = select(Robot).order_by(Robot.id)
    result = await session.execute(stmt)
    robots = result.scalars().all()
    return list(robots)


async def get_robot(session: AsyncSession, robot_id) -> Robot | None:
    return await session.get(Robot, robot_id)


async def update_robot_status(session: AsyncSession, robot_id: int) -> Robot:
    stmt = select(Robot).where(Robot.id == robot_id)
    result = await session.execute(stmt)
    robot = result.scalars().first()

    if not robot:
        raise HTTPException(status_code=404, detail="Robot not found")

    if robot.status == "delivery":
        robot.status = "delivery_completed"

    if robot.status == "delivery_completed":
        robot.status = "sleep"

    if robot.status == "sleep":
        robot.status = "delivery"

    await session.commit()
    await session.refresh(robot)

    return robot


async def update_robot_deliver(
    session: AsyncSession, robot_id: int, room_id: int
) -> Robot:
    stmt = select(Robot).where(Robot.id == robot_id)
    result = await session.execute(stmt)
    robot = result.scalars().first()

    if not robot:
        raise HTTPException(status_code=404, detail="Robot not found")

    robot.deliver = True
    robot.deliver_status = "delivery"
    robot.deliver_room = room_id

    await session.commit()
    await session.refresh(robot)

    return robot


async def get_deliveries(session: AsyncSession) -> list[Robot]:
    stmt = select(Robot).filter(Robot.deliver == True)
    result = await session.execute(stmt)
    robots = result.scalars().all()
    return list(robots)


async def get_delivery(session: AsyncSession, robot_id) -> Robot | None:
    return await session.get(Robot, robot_id)
