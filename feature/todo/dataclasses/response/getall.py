from dataclasses import dataclass
from typing import List

@dataclass
class TodoGetAllItem:
    id: int
    title: str
    description: str
    completed: bool
    createdAt: str
    updatedAt: str

@dataclass
class TodoGetAllResponse:
    results: List[TodoGetAllItem]
    page_num: int
    total_page: int
    total_count: int
    next_page_required: bool
