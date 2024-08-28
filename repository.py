from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.sql.annotation import Annotated

from database import TaskORM, new_session
from schemas import STaskAdd, STask, STaskID


class TaskRepository:
    @classmethod
    async def add_one(cls, task: STaskAdd) -> STaskID:
        async with new_session() as session:
            data = task.model_dump()
            new_task = TaskORM(**data)
            session.add(new_task)
            await session.flush()
            await session.commit()
            return new_task.id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [STask.model_validate(task_model) for task_model in task_models]
            return tasks
