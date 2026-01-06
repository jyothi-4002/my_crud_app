from dataclasses import dataclass
from .base import BaseResponseDataclass

@dataclass
class ArtistCreateResponseDataclass(BaseResponseDataclass):
    id: int
    name: str
    age: int
    createdAt: str
