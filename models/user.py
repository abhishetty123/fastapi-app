from sqlalchemy import create_engine

from sqlalchemy.orm import  Mapped, mapped_column
from core .database import Base

class User(Base):
    __tablename__ = "users"
    id : Mapped[int] = mapped_column (primary_key=True, index=True)
    name : Mapped[str] = mapped_column( index=True)
    email : Mapped[str] = mapped_column(unique=True, index=True)
    password : Mapped[str] = mapped_column( index=True)