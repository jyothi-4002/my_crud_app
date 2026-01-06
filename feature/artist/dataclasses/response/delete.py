from dataclasses import dataclass
from typing import List
from .base import BaseResponseDataclass

@dataclass
class ArtistDeleteResponseDataclass(BaseResponseDataclass):
    deleted_ids: List[int]
