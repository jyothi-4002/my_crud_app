from dataclasses import dataclass
from typing import List, Optional
from .base import BaseResponseDataclass

@dataclass
class ArtistGetAllItemResponseDataclass(BaseResponseDataclass):
    id: int
    name: str
    age: int
    createdAt: str


@dataclass
class ArtistGetAllResponseDataclass(BaseResponseDataclass):
    data: List[ArtistGetAllItemResponseDataclass]
    presentPage: int
    totalPage: int
    totalCount: int
    nextPageUrl: Optional[str] = None
