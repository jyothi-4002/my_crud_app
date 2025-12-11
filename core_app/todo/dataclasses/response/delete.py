
from dataclasses import dataclass
from typing import List

@dataclass
class TodoDeleteResponse:
    deleted_ids: List[int]
