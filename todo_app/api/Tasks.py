from todo_app.db.models import Tasks
from todo_app.db.schema import TaskCreateSchema, TaskOutSchema, TaskUpdateSchema
from typing import List
from fastapi import APIRouter, HTTPException


task_router = APIRouter(prefix='/tasks', tags=['Tasks'])

@task_router.post('/', response_model=dict)
async def create_task(task: TaskCreateSchema):
    task_db = Tasks(**task.model_dump())
    await task_db.insert()
    return {'message': 'Saved'}


@task_router.get('/', response_model=List[TaskOutSchema])
async def list_task():
    task_db = await Tasks.all().to_list()
    return [TaskOutSchema(id=str(task.id), **task.model_dump(exclude={'id'}))for task in task_db]


@task_router.get('/{task_id}', response_model=TaskOutSchema)
async def detail_task(task_id: str):
    task_db = await Tasks.get(task_id)
    if not task_db:
        raise HTTPException(status_code=404, detail='Tasks not found')
    return TaskOutSchema(id=str(task_id), **task_db.model_dump(exclude={'id'}))


@task_router.put('/{task_id}', response_model=dict)
async def update_task(task_id: str, task_update: TaskUpdateSchema):
    task_db = await Tasks.get(task_id)
    if not task_db:
        raise HTTPException(status_code=404, detail='Task not found')

    task_data = task_update.model_dump(exclude_unset=True)
    await task_db.update({'$set': task_data})
    return {'message': 'Upgraded', 'id': task_id}

@task_router.delete('/{task_id}', response_model=dict)
async def delete_task(task_id: str):
    task_db = await Tasks.get(task_id)
    if not task_db:
        raise HTTPException(status_code=404, detail='Tasks not found')
    await task_db.delete()
    return {'message': 'This tasks is deleted'}









