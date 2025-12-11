from dataclasses import dataclass
from typing import List, Optional

@dataclass
class TodoDeleteRequest:
    id: Optional[int] = None
    ids: Optional[List[int]] = None
