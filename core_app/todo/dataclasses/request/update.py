from dataclasses import dataclass
from typing import Optional

@dataclass
class TodoUpdateRequest:
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
