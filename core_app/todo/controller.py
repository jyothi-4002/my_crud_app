# core_app/todo/controller.py
from django.core.exceptions import ObjectDoesNotExist
from core_app.todo.models.todo import TodoItem
from core_app.todo.dataclasses.request import TodoRequest
from core_app.todo.dataclasses.response import TodoResponse

def create_todo(data: TodoRequest) -> TodoResponse:
    todo = TodoItem.objects.create(
        title=data.title,
        description=data.description,
        completed=data.completed
    )
    return TodoResponse(
        id=todo.id,
        title=todo.title,
        description=todo.description or "",
        completed=todo.completed,
        created_at=todo.created_at.isoformat(),
        updated_at=todo.updated_at.isoformat()
    )

def get_all_todos():
    todos = TodoItem.objects.all().order_by('-created_at')
    return [TodoResponse(
        id=t.id,
        title=t.title,
        description=t.description or "",
        completed=t.completed,
        created_at=t.created_at.isoformat(),
        updated_at=t.updated_at.isoformat()
    ) for t in todos]

def get_todo_by_id(todo_id: int):
    try:
        todo = TodoItem.objects.get(id=todo_id)
    except ObjectDoesNotExist:
        return None
    return TodoResponse(
        id=todo.id,
        title=todo.title,
        description=todo.description or "",
        completed=todo.completed,
        created_at=todo.created_at.isoformat(),
        updated_at=todo.updated_at.isoformat()
    )

def update_todo(todo_id: int, data: TodoRequest):
    try:
        todo = TodoItem.objects.get(id=todo_id)
    except ObjectDoesNotExist:
        return None
    # update only fields present in dataclass (we expect full object for now)
    if data.title is not None:
        todo.title = data.title
    todo.description = data.description
    todo.completed = data.completed
    todo.save()
    return TodoResponse(
        id=todo.id,
        title=todo.title,
        description=todo.description or "",
        completed=todo.completed,
        created_at=todo.created_at.isoformat(),
        updated_at=todo.updated_at.isoformat()
    )

def delete_todo(todo_id: int):
    try:
        todo = TodoItem.objects.get(id=todo_id)
    except ObjectDoesNotExist:
        return False
    todo.delete()
    return True
