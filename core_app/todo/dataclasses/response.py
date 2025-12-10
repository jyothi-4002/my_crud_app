# core_app/todo/dataclasses/response.py
from dataclasses import dataclass

@dataclass
class TodoResponse:
    id: int
    title: str
    description: str
    completed: bool
    created_at: str
    updated_at: str
