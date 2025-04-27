from datetime import datetime
from typing import Optional, List
from enum import Enum
from beanie import Link, Document


class Users(Document):
    email: str
    first_name: str
    username: str
    password: str
    created_at: datetime = datetime.utcnow()
    user_tasks: Optional[List[Link['Tasks']]] = None


    class Settings:
        name = 'users'

class StatusChoices(str, Enum):
    to_do = 'to_do'
    in_progress = 'in_progress'
    done = 'done'
    expired = 'expired'


class Tasks(Document):
    user: Optional[Link[Users]] = None
    title: str
    description: str
    deadline: datetime
    status: StatusChoices = StatusChoices.to_do
    created_at: datetime = datetime.utcnow()

    class Settings:
        name = 'tasks'



