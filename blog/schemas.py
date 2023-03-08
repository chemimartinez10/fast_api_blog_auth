from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    id:Optional[int]
    title:str
    content:str
    published:Optional[bool]

    class Config:
        orm_mode = True

class BlogUpdate(BaseModel):
    title:Optional[str] | None
    content:Optional[str] | None
    published:Optional[bool] | None