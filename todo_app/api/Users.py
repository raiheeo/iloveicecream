from todo_app.db.models import Users
from todo_app.db.schema import UserCreateSchema, UserOutSchema, UserUpdateSchema
from fastapi import APIRouter, HTTPException
from typing import List


user_router = APIRouter(prefix='/users', tags=['Users'])

@user_router.post('/', response_model=dict)
async def create_user(user: UserCreateSchema):
    user_db = Users(**user.model_dump())
    await user_db.insert()
    return {'message': 'Saved'}

@user_router.get('/', response_model=List[UserOutSchema])
async def list_user():
    users = await Users.all().to_list()
    return [UserOutSchema(id=str(user.id), **user.model_dump(exclude={'id'})) for user in users]

@user_router.get('/{user_id}', response_model=UserOutSchema)
async def detail_user(user_id: str):
    user_db = await Users.get(user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail='User not found')
    return UserOutSchema(id=str(user_db.id), **user_db.model_dump(exclude={'id'}))

@user_router.put('/{user_id}',response_model=dict)
async def update_user(user_id: str, user_update: UserUpdateSchema):
    user_db = await Users.get(user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail='User not found')

    user_data = user_update.model_dump(exclude_unset=True)
    await user_db.update({'$set': user_data})
    return {'message': 'Upgraded', 'id': user_id}


@user_router.delete('/{user_id}', response_model=dict)
async def delete_user(user_id: str):
    user_db = await Users.get(user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail='User not found')
    await user_db.delete()
    return {'message': 'This user is deleted'}






















