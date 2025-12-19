from dataclasses import dataclass

@dataclass
class TodoCreateResponse:
    id: int
    title: str
    description: str
    completed: bool
    createdAt: str
    updatedAt: str
