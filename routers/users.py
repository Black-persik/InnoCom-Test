from fastapi import APIRouter
from sqlalchemy import UUID

import utils.users as users_utils
from shemas import users
from fastapi import HTTPException
router = APIRouter()

@router.post('/create-user', response_model=users.CreateUser, status_code=201)
async def create_user(user: users.CreateUser):
    return await users_utils.create_user(user)

@router.get('/get-user/{user_id}', status_code=200)
async def get_user(user_id: str):
    return await users_utils.get_user(user_id)
