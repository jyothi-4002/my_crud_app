from dataclasses import dataclass
from typing import Optional

@dataclass
class MusicUpdateRequest:
    id: int
    artist_id: Optional[int] = None
    title: Optional[str] = None
    singer: Optional[str] = None
    writer: Optional[str] = None
    description: Optional[str] = None
    released_date: Optional[str] = None
