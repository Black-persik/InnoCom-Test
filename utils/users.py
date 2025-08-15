from sqlalchemy import UUID

from models.database import database as db
from shemas.users import User, CreateUser
from models.users import users_table
async def create_user(user: CreateUser) -> dict:
    query = (
        users_table.insert()
        .values(
            email=user.email,
            username=user.username,
        ).returning(users_table.c.user_id)
    )
    post = await db.fetch_one(query)
    post = dict(zip(post, post.values()))
    return post

async def get_user(user_id:str):
    query = (
        users_table.select()
        .where(users_table.c.user_id == user_id)
    )
    get = db.fetch_one(query)
    return await get