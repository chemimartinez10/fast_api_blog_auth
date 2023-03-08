from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base
from typing import Optional

class Blog(Base):
    __tablename__ = "blogs"
    
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title:Mapped[str] = mapped_column(String(40), unique=True)
    content:Mapped[str] = mapped_column(String)
    published:Mapped[Optional[bool]] = mapped_column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"Blog(id={self.id!r}, title={self.title!r}, published={self.published!r})"
