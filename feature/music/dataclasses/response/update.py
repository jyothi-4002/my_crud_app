from dataclasses import dataclass

@dataclass
class MusicUpdateResponse:
    id: int
    title: str
    singer: str
    writer: str
    description: str
    createdAt: str
