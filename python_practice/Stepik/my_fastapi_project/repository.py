from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from python_practice.Stepik.my_fastapi_project.models.tasks import TasksModel
from python_practice.Stepik.my_fastapi_project.schemas.task import STaskAdd
class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd, session:AsyncSession) -> TasksModel:
        # 1. Превращаем данные из pydantic в словарь
        task_dict  = data.model_dump()

        # 2. Создаём объект модели
        task = TasksModel(**task_dict)

        # 3. Добвляем и сохраняем
        session.add(task)
        await session.commit()
        await session.refresh(task)


        # 4. Возвращем созданный объект
        return task

    @classmethod
    async def find_all(cls, session: AsyncSession):
        # 1. Готовим запрос
        query = select(TasksModel)

        # 2. Выполняем
        result = await session.execute(query)


        # 3. Возвращаем список объектов
        task_models = result.scalars().all()
        return task_models