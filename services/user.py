from sqlalchemy.orm import Session
from sqlalchemy.engine import RowMapping
from sqlalchemy import select, text
from models.user import User as UserModel
from shemas.user import AddUser

def create_user_service(user:AddUser, db: Session):
    new_user = UserModel(name=user.name, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# legacy code
def get_user_by_id_service(user_id:int, db:Session):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    return user

# modern code
def get_user_by_mail_service(user_mail: str, db:Session) -> UserModel | None:  
    statement = select(UserModel).where(UserModel.email == user_mail)
    return db.scalar(statement)

#raw Querry 
def get_user_by_mail_raw(user_mail:str, db:Session) -> RowMapping | None:
    statement = text("""
            SELECT *
            FROM users
            WHERE email = :email
            LIMIT 1
        """)
    return db.execute(
        statement,
        {"email": user_mail}
    ).mappings().first()
    