from pydantic import BaseModel, EmailStr, UUID4


class User(BaseModel):
    user_id: UUID4
    email: EmailStr
    username: str

class CreateUser(BaseModel):
    email: EmailStr
    username: str