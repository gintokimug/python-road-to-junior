from database import ModelB, engine
from contextlib import asynccontextmanager
from routers.books import router 

from fastapi import FastAPI



@asynccontextmanager
async def lifespan(app : FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(ModelB.metadata.create_all)

    print("Список книг готов")

    yield

    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(router)
