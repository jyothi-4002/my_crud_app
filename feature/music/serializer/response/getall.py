from dataclasses import dataclass
from typing import List, Optional
from .base import BaseResponseDataclass

@dataclass
class MusicGetAllItemResponseDataclass(BaseResponseDataclass):
    id: int
    title: str
    singer: str
    writer: str
    description: Optional[str]
    released_date: Optional[str]
    createdAt: str


@dataclass
class MusicGetAllResponseDataclass(BaseResponseDataclass):
    data: List[MusicGetAllItemResponseDataclass]
    presentPage: int
    totalPage: int
    totalCount: int
    nextPageUrl: Optional[str] = None
