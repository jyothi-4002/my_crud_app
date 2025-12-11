from dataclasses import dataclass

@dataclass
class TodoUpdateResponse:
    id: int
    title: str
    description: str
    completed: bool
    created_at: str
    updated_at: str
