from dataclasses import dataclass

@dataclass
class TodoUpdateResponse:
    id: int
    title: str
    description: str
    completed: bool
    createdAt: str
    updatedAt: str
