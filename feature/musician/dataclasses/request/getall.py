from dataclasses import dataclass


@dataclass
class MusicianGetAllDC:
    page_num: int = 1
    limit: int = 10
