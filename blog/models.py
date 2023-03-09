from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base
from typing import Optional

class User(Base):
    __tablename__ = "users"
    
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(40))
    email:Mapped[str] = mapped_column(String, unique=True)
    password:Mapped[str] = mapped_column(String)

    blogs:Mapped[list['Blog']] = relationship(back_populates='author')

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"

class Blog(Base):
    __tablename__ = "blogs"
    
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title:Mapped[str] = mapped_column(String(40), unique=True)
    content:Mapped[str] = mapped_column(String)
    published:Mapped[Optional[bool]] = mapped_column(Boolean, default=False)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id", name="fk_blog_user_id"))

    author:Mapped['User'] = relationship(back_populates='blogs')

    def __repr__(self) -> str:
        return f"Blog(id={self.id!r}, title={self.title!r}, published={self.published!r})"
    
