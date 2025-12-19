from dataclasses import dataclass
from typing import Optional

@dataclass
class MusicUpdateRequest:
    id: int
    title: Optional[str] = None
    singer: Optional[str] = None
    writer: Optional[str] = None
    description: Optional[str] = None
