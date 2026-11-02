from pydantic import BaseModel, EmailStr


class AddUser(BaseModel):
    name:str
    email:EmailStr
    password:str

class UserUpdate(BaseModel):
    name:str | None
    email:EmailStr | None
    password:str | None