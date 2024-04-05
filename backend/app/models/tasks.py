from typing import Any

from pydantic import BaseModel

class Task(BaseModel):
    task_id: str

class TaskCreate(Task):
    pass
class TaskResult(Task):
    task_status: str
    task_result: Any

class SampeTaskPayload(BaseModel):
    type: int