from .models.todo import TodoItem
from .serializers.request import TodoRequest
from .serializers.response import TodoResponse

def create_todo(data: TodoRequest) -> TodoResponse:
    todo = TodoItem.objects.create(
        title=data.title,
        description=data.description,
        completed=data.completed
    )
    return TodoResponse(
        id=todo.id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        created_at=str(todo.created_at),
        updated_at=str(todo.updated_at)
    )

def get_all_todos():
    todos = TodoItem.objects.all()
    return [TodoResponse(
        id=t.id,
        title=t.title,
        description=t.description,
        completed=t.completed,
        created_at=str(t.created_at),
        updated_at=str(t.updated_at)
    ) for t in todos]

def get_todo_by_id(todo_id: int):
    todo = TodoItem.objects.get(id=todo_id)
    return TodoResponse(
        id=todo.id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        created_at=str(todo.created_at),
        updated_at=str(todo.updated_at)
    )

def update_todo(todo_id: int, data: TodoRequest):
    todo = TodoItem.objects.get(id=todo_id)
    todo.title = data.title
    todo.description = data.description
    todo.completed = data.completed
    todo.save()
    return TodoResponse(
        id=todo.id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        created_at=str(todo.created_at),
        updated_at=str(todo.updated_at)
    )

def delete_todo(todo_id: int):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return {"message": "Todo deleted successfully"}
