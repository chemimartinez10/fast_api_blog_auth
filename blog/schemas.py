from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name:str
    email:str
    password:str

    class Config:
        orm_mode = True

class Blog(BaseModel):
    title:str
    content:str
    published:Optional[bool]
    user_id:int

    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    name:str
    email:str
    blogs:list[Blog] = []

    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title:str
    content:str
    author:ShowUser

    class Config:
        orm_mode = True

class BlogUpdate(BaseModel):
    title:Optional[str] | None
    content:Optional[str] | None
    published:Optional[bool] | None

class Login(BaseModel):
    username:str
    password:str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None