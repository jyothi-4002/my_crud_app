from dataclasses import dataclass
from typing import Optional

@dataclass
class TodoGetRequest:
    id: Optional[int] = None
