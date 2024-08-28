from typing import Optional, Annotated

from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as task_router
from schemas import STaskAdd


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена.")
    await create_tables()
    print("База готова.")
    yield
    print("Выключение...")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
