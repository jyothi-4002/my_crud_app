from dataclasses import dataclass

@dataclass
class TodoCreateResponse:
    id: int
    title: str
    description: str
    completed: bool
    created_at: str
    updated_at: str
