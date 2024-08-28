from fastapi import APIRouter, Depends
from sqlalchemy.sql.annotation import Annotated

from repository import TaskRepository
from schemas import STask, STaskAdd, STaskID


router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)


@router.post("")
async def add_task(task: STaskAdd = Depends()) -> STaskID:
    new_task_id = await TaskRepository.add_one(task)
    return {"ok": True, "id": new_task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return tasks
