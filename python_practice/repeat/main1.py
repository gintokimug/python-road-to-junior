from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Task(BaseModel):
    tittle : str
    description : str | None = None
    is_completed : bool = False 

@app.post("/tasks/")
def create_task(task : Task):
    return {
        "message" : "Задача успешно создана",
        "task" : task 
    }

@app.get("/")
def read_root():
    return {"message": "Привет, Хабр!"}


@app.get("/tasks")
def get_tasks(skip: int = 0, limit: int = 10):
    return {
        "message": "Возвращаем список задач",
        "skip": skip,
        "limit": limit
    }


