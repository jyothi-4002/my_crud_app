from dataclasses import dataclass
from typing import List
from .base import BaseResponseDataclass

@dataclass
class MusicDeleteResponseDataclass(BaseResponseDataclass):
    deleted_ids: List[int]
