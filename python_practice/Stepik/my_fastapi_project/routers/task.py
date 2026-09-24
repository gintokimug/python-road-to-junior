# from fastapi import APIRouter, Depends
# from typing import Annotated

# from sqlalchemy import select

# from models.tasks import TasksModel
# from  schemas.task import STask, STaskAdd
# from database import SessionDep # Импортируем нашу зависимость


# router = APIRouter(
#     prefix="/tasks", 
#     tags=["Задачи"])



# @router.post("", response_model=STask)
# async def create_task(
#     task: STaskAdd,
#     session: SessionDep, # <--- Внедрение зависимости
# ):
#     # Теперь внутри функции у нас есть переменная session
#     # Это готовое подключени к базе данных

#     # 1 Превращаем Pydantic - схему в модель БД
#     # task.model_dump() вернёт словарь {"name" : "...", ...}
#     # ** - это распаковка словаря
#     new_task = TasksModel(**task.model_dump())

#     # 2. Добавляем в сессию 
#     session.add(new_task)

#     # 3. Коммитим( сохраняем на диск)
#     await session.commit()

#     # 4. Обновляем объект(получаем выданный ID)
#     await session.refresh(new_task)

#     # 5. Возвращаем объект БД. Pydantic сам превратит его в JSON
#     return new_task

# @router.get("")
# async def get_tasks(
#     session: SessionDep # <--- Здесь тоже
# ):
#     # 1. Формируем запрос
#     query = select(TasksModel)

#     # 2. Выполняем запрос
#     result = await session.execute(query)

#     # 3. Получаем чистые объекты (scalars) и превращаем в список (all)
#     return result.scalars().all()



from fastapi import APIRouter
from typing import Annotated

from python_practice.Stepik.my_fastapi_project.database import SessionDep
from python_practice.Stepik.my_fastapi_project.schemas.task import STask, STaskAdd
from python_practice.Stepik.my_fastapi_project.repository import TaskRepository #Импортируем наш новый класс

router = APIRouter(prefix="/tasks", tags = ["Задачи"])

@router.post("", response_model=list[STask])
async def create_task(
    task: STaskAdd,
    session: SessionDep
):
    # Вся логика сохранения ушла в репозиторий
    #Роутер просто передаёт данные и ждёт результат
    task_model = await TaskRepository.add_one(task,session)
    return task_model


@router.get("", response_model = list[STask])
async def get_tasks(
    session: SessionDep
):
    #HРоутер не знает, как выпоняются задачи (SQL? API? ФАЙЛ?)
    # Нужен только список задач
    tasks = await TaskRepository.find_all(session)
    return tasks