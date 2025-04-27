from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from .models import StatusChoices


class UserCreateSchema(BaseModel):
    email: EmailStr
    first_name: str
    username: str
    password: str

class UserOutSchema(BaseModel):
    id: str
    email: EmailStr
    first_name: str
    username: str
    created_at: datetime


class TaskCreateSchema(BaseModel):
    title: str
    description: str
    deadline: datetime


class TaskOutSchema(BaseModel):
    id: str
    title: str
    description: str
    deadline: datetime
    status: StatusChoices
    created_at: datetime
    user: Optional[int]

class TaskUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    status: Optional[StatusChoices] = None


class UserUpdateSchema(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    username: Optional[str] = None
    password: str


