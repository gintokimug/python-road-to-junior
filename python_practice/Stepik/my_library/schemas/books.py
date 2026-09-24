from pydantic import BaseModel, ConfigDict,Field

class SBookAdd(BaseModel): # (для создания/обновления)
    title : str
    author : str
    year : int
    pages : int = Field(gt=10)
    is_read : bool = False

class Sbook(SBookAdd): # (для возврату клиенту)
    id : int 

    model_config = ConfigDict(from_attributes=True)

