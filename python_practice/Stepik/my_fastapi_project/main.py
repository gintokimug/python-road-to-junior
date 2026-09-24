from contextlib import asynccontextmanager
from python_practice.Stepik.my_fastapi_project.database import engine,Model 

from fastapi import FastAPI
from python_practice.Stepik.my_fastapi_project.routers.task import router as tasks_router
from python_practice.Stepik.my_fastapi_project.models.tasks import TasksModel




@asynccontextmanager
async def lifespan(app: FastAPI):
    #ОБращение к движку создать все таблицы
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

        print ("База данных готова к работе ")

        yield # разделяет старт и выключение

        # --- КОД ПРИ ВЫКЛЮЧЕНИИ
        print("Выключение сервера")

        #Передаём Lifespan  в приложении

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)





# import unicorn
# from fastapi import FastAPI,HTTPException,status
# from router import router as tasks_router

# app = FastAPI()

# app.include_router(users.router)
# app.include_router(catalog.router)

# @app.get("/")
# def welcome():
#     return {"message" : "ку ку"}
# if __name__ == "main":
#     unicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# tasks = {
#     1: {"name": "Laptop", "price": 1000},
#     2: {"name": "Mouse", "price": 20}
# }

# @app.put("/tasks/{item_id}")
# async def new_price(item_id : int, price : int):
#     if item_id not in tasks:
#         raise HTTPException(
#             status_code = status.HTTP_404_NOT_FOUND)
#     else:
#         tasks[item_id]["price"] = price
#         return tasks[item_id]


# @app.delete("/tasks/{task_id}", status_code = status.HTTP_404)
# async def delete_task(task_id : int):
#     for index, task in enumerate(tasks):
#         if task["id"] == task_id:
#             tasks.pop(index)
#             return
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Задача не найдена"
#         )


