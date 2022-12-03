
from pydantic import BaseModel

from src.position import Position


class User(BaseModel):
    id: str
    socket_id: str
    position: Position

    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id

    def __hash__(self):
        return self.id.__hash__()
