from fastapi import FastAPI
from routers import users as users_router
from routers import snippets as snippets_router
from models.database import database
app = FastAPI()

app.include_router(users_router.router)
app.include_router(snippets_router.router)
@app.get('/')
async def root():
    return {'message': 'Hello World'}
@app.on_event('startup')
async def startup():
    await database.connect()
@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()