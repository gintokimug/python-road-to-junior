from fastapi import APIRouter,status, HTTPException
from typing import Annotated


from database import SessionDep
from schemas.books import SBookAdd,Sbook
from repository import BookRepository


router = APIRouter(prefix="/books", tags = ["Книги"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=Sbook) 
async def add_book(
        book: SBookAdd,
        session: SessionDep
) -> Sbook:
    result = await BookRepository.add_book(book,session)
    return result 


@router.get("", response_model=list[Sbook], status_code=status.HTTP_200_OK)
async def get_all_books( session: SessionDep):
    books = await BookRepository.find_all(session)
    return books

@router.get("/{book_id}", response_model=Sbook)
async def get_one_book(book_id : int, session: SessionDep) -> Sbook:
# поиск книги в репозитории 
    book = await BookRepository.find_one_or_none(book_id,session)

    if not book:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Книга не найдена"
        )
    return book 
    

@router.put("/{book_id}",
            response_model=Sbook,
            status_code=status.HTTP_200_OK
            )
async def update_one_book(
    book_id : int,
    book_data: SBookAdd,
    session : SessionDep):
    update_book = await BookRepository.update_one(book_id,book_data,session)
    if not update_book:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND
        )
    return update_book 

@router.delete("/{book_id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_one_book(
    book_id : int,
    session : SessionDep
    ):
    delete_book = await BookRepository.delete_one(book_id,session)
    if not delete_book:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND
        )
    return None 
    



