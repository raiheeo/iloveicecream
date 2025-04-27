from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from todo_app.db.database import init_db
from todo_app.api import Users, Tasks


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

todo_app = FastAPI(title='ToDo Site')
todo_app.include_router(Users.user_router)
todo_app.include_router(Tasks.task_router)

if __name__ == '__main__':
    uvicorn.run(todo_app, host='127.0.0.1', port=8001)

