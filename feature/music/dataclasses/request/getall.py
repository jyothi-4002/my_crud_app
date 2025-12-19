from dataclasses import dataclass

@dataclass
class MusicGetAllRequest:
    page_num: int = 1
    limit: int = 10
