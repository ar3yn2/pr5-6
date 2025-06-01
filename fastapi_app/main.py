from fastapi import FastAPI
from fastapi_app.database import database
from fastapi_app import crud, schemas

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate):
    user_id = await crud.create_user(user)
    return {"id": user_id, **user.dict()}

@app.get("/users/", response_model=list[schemas.User])
async def read_users():
    return await crud.get_users()
