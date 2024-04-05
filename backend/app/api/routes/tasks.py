from fastapi import APIRouter, Body

from celery.result import AsyncResult

from app.tasks.sample import create_task
from app.models.tasks import TaskResult, TaskCreate, SampeTaskPayload


router = APIRouter()

@router.post("/sampletask", status_code=201, response_model=TaskCreate)
def run_task(payload: SampeTaskPayload):
    task = create_task.delay(payload.type)
    return TaskCreate(task_id=task.id)

@router.get("/tasks/{task_id}", response_model=TaskResult)
def get_status(task_id: str):
    task_result = AsyncResult(task_id)
    result = TaskResult(
        task_id=task_id,
        task_status=task_result.status,
        task_result=task_result.result
    )
    return result