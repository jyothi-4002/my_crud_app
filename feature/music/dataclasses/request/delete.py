from dataclasses import dataclass
from typing import List

@dataclass
class MusicDeleteRequest:
    ids: List[int]
