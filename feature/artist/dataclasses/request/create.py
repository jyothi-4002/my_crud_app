from dataclasses import dataclass
from typing import Optional

@dataclass
class ArtistCreateRequest:
    name: str
    age: int
    description: Optional[str] = None
    debut_date: Optional[str] = None
