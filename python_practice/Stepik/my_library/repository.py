from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.books import Bookmodel
from schemas.books import SBookAdd

class BookRepository:
    @classmethod
    async def add_book(cls, data : SBookAdd, session : AsyncSession) -> Bookmodel:
        book_dict = data.model_dump()

        book = Bookmodel(**book_dict)


        session.add(book)
        await session.commit()
        await session.refresh(book)

        return book

    @classmethod
    async def find_one_or_none(
        cls,
        book_id : int,
        session: AsyncSession) -> Bookmodel:
        query = select(Bookmodel).where(Bookmodel.id == book_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_all (cls, session : AsyncSession):
        query = select(Bookmodel)
        result = await session.execute(query)
        return result.scalars().all()


    @classmethod
    async def update_one(
        slc,
        book_id : int,
        data : SBookAdd,
        session : AsyncSession
    ) -> Bookmodel | None:
        # поиск по существующему id
        query = select(Bookmodel).where(Bookmodel.id == book_id)
        result = await session.execute(query)
        book = result.scalar_one_or_none()

        if not book: 
            return None
        for key,value in data.model_dump().items():
            setattr(book,key,value)

        await session.commit()
        await session.refresh(book)
        return book 

    @classmethod
    async def delete_one(
        cls,
        book_id : int,
        session : AsyncSession
    ) -> bool:
        query = select(Bookmodel).where(Bookmodel.id == book_id)
        result = await session.execute(query)
        book = result.scalar_one_or_none()

        if not book:
            return False

        await session.delete(book)
        await session.commit()
        return True
        
        

    

