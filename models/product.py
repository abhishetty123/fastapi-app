from sqlalchemy import create_engine

from sqlalchemy.orm import  Mapped, mapped_column
from core .database import Base

class Product(Base):
    __tablename__ = "products"
    id : Mapped[int] = mapped_column (primary_key=True, index=True)
    name : Mapped[str] = mapped_column( index=True)
    price : Mapped[float] = mapped_column( index=True)
    category : Mapped[str] = mapped_column( index=True)
    qty: Mapped[int] = mapped_column(index=True,default=0,server_default="0",)
