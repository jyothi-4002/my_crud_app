from dataclasses import dataclass
from typing import Optional

@dataclass
class MusicCreateRequest:
    title: str
    singer: str
    writer: str
    description: Optional[str] = None
    released_date: Optional[str] = None
