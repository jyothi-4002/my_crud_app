from dataclasses import dataclass

@dataclass
class TodoCreateRequest:
    title: str
    description: str = ""
    completed: bool = False
