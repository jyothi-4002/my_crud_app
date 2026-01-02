from dataclasses import dataclass
from typing import Optional


@dataclass
class MusicianUpdateDC:
    id: int
    name: Optional[str] = None
    age: Optional[int] = None
