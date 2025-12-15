from dataclasses import dataclass

@dataclass
class TodoGetAllRequest:
    page_num: int = 1
    limit: int = 50
