from pydantic import BaseModel, Field


class STaskAdd(BaseModel):
    name: str  = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Название задачи"
        )    
    desciption: str | None = Field(None, max_length=300)
    priority = int = Field(ge=1, le=5)