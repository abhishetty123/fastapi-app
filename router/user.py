from fastapi import APIRouter, Depends
from typing import Annotated
from services.user import create_user_service,get_user_by_mail_service,get_user_by_id_service
from sqlalchemy.orm import Session
from shemas.user import AddUser
from core.database import get_db, Base
from models.user import User as UserModel

db_dependancy =  Annotated[Session, Depends(get_db)]
router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/create")
def create_user(user: AddUser, db: db_dependancy):
    return create_user_service(user, db)

@router.get("/user_id")
def get_user_by_id(user_id: int, db:db_dependancy):
    return get_user_by_id_service(user_id, db)

@router.get("/user_mail")
def get_userby_mail(user_mail : str, db: db_dependancy):
    return get_user_by_mail_service(user_mail, db)