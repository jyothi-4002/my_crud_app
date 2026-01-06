from dataclasses import dataclass
from .base import BaseResponseDataclass

@dataclass
class ArtistUpdateResponseDataclass(BaseResponseDataclass):
    id: int
    name: str
    age: int
    createdAt: str
