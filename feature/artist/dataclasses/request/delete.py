from dataclasses import dataclass
from typing import List

@dataclass
class ArtistDeleteRequest:
    ids: List[int]
