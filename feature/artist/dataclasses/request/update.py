from dataclasses import dataclass
from typing import Optional

@dataclass
class ArtistUpdateRequest:
    id: int
    name: Optional[str] = None
    age: Optional[int] = None
    description: Optional[str] = None
    debut_date: Optional[str] = None
