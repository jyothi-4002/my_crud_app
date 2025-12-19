from dataclasses import dataclass

@dataclass
class TodoGetResponse:
    id: int
    title: str
    description: str
    completed: bool
    createdAt: str
    updatedAt: str
