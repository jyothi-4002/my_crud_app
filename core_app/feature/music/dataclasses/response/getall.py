from dataclasses import dataclass
from typing import List, Optional


@dataclass
class MusicGetAllItemResponse:
    id: int
    title: str
    singer: str
    writer: str
    description: Optional[str]
    released_date: Optional[str]
    createdAt: str


@dataclass
class MusicGetAllResponse:
    data: List[MusicGetAllItemResponse]
    presentPage: int
    totalPage: int
    totalCount: int
    nextPageUrl: Optional[str] = None
