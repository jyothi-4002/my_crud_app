from dataclasses import dataclass

@dataclass
class MusicGetResponse:
    id: int
    title: str
    singer: str
    writer: str
    description: str
    createdAt: str
