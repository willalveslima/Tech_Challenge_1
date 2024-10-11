from typing import Optional

from pydantic import BaseModel, EmailStr, validator

from app.utils.authenticator import Authenticator


class User(BaseModel):
    name: str
    email: EmailStr
    password: str


    @validator("password")
    def hash_password(cls, password: str):
        authenticator = Authenticator()
        return authenticator.get_hashed_password(password)


class UserCreated(BaseModel):
    id: int
    name: Optional[str]
    email: Optional[EmailStr]

    class Config:
        orm_mode = True


class UserToken(BaseModel):
    access_token: Optional[str]
    user: Optional[str]
    exp: Optional[str]