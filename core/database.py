from sqlalchemy import  Integer, create_engine
from sqlalchemy.orm import  Mapped,mapped_column, declarative_base, sessionmaker
from os import getenv

DATABASE_URL = getenv("DATABASE_URL")
engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    echo=False
    )
Base = declarative_base()





SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
