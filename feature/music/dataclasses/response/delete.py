from dataclasses import dataclass
from typing import List

@dataclass
class MusicDeleteResponse:
    deleted_ids: List[int]

