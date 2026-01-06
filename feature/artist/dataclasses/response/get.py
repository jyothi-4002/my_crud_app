from dataclasses import dataclass
from .base import BaseResponseDataclass

@dataclass
class ArtistGetResponseDataclass(BaseResponseDataclass):
    id: int
    name: str
    age: int
    createdAt: str
