from collections import defaultdict

from pydantic import BaseModel

from src.connection import Connection


class ConnectionStorage(BaseModel):
    users_to_connections: dict[str, list[Connection]] = defaultdict(lambda: [])

    def __getitem__(self, item: str) -> list[Connection]:
        return self.users_to_connections[item]
