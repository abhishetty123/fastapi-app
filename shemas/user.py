from pydantic import BaseModel, EmailStr


class AddUser(BaseModel):
    name:str
    email:EmailStr
    password:str