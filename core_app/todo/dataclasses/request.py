# core_app/todo/dataclasses/request.py
from dataclasses import dataclass

@dataclass
class TodoRequest:
    title: str
    description: str = ""
    completed: bool = False
