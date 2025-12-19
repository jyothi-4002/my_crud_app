from dataclasses import dataclass
from typing import Optional
from .base import BaseResponseDataclass

@dataclass
class MusicGetResponseDataclass(BaseResponseDataclass):
    id: int
    title: str
    singer: str
    writer: str
    description: Optional[str]
    released_date: Optional[str]
    createdAt: str
