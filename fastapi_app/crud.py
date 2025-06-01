from fastapi_app.schemas import UserCreate
from fastapi_app.models import users
from fastapi_app.database import database

async def create_user(user: UserCreate):
    query = users.insert().values(name=user.name, email=user.email)
    return await database.execute(query)

async def get_users():
    query = users.select()
    return await database.fetch_all(query)