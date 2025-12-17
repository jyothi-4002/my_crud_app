from dataclasses import dataclass
from typing import Optional


@dataclass
class MusicCreateResponse:
    id: int
    title: str
    singer: str
    writer: str
    description: Optional[str]
    released_date: Optional[str]
    createdAt: str
