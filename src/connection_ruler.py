from math import sqrt
from typing import Protocol

from shapely.geometry import LineString, Point

from src.connection import Connection
from src.position import Position
from src.room_layout import RoomLayout
from src.user import User


class ConnectionRuler(Protocol):
    def get_connection_type(self, client: User, communication_partner: User) -> Connection:
        pass


class ConnectionBasedOnRange(ConnectionRuler):
    def __init__(self, socket_range: float, nakama_range: float, room_layout: RoomLayout) -> None:
        self._room_layout = room_layout
        self._socket_range = socket_range
        self._nakama_range = nakama_range

    def get_connection_type(self, client: User, communication_partner: User) -> None | Connection:
        distance = sqrt(
            pow(client.position.x - communication_partner.position.x, 2) +
            pow(client.position.y - communication_partner.position.y, 2) +
            pow(client.position.z - communication_partner.position.z, 2)
        )
        if self._is_in_line_of_sight(client.position, communication_partner.position) is False:
            return None
        if distance <= self._socket_range:
            return Connection(type='socket',
                              address=communication_partner.socket_id,
                              target_id=communication_partner.id)
        if distance <= self._nakama_range:
            return Connection(type='nakama',
                              address='basic-nakama',
                              target_id=communication_partner.id)
        return None

    def _is_in_line_of_sight(self, first_position: Position, second_position: Position) -> bool:
        connection_line = LineString([(first_position.x, first_position.y), (second_position.x, second_position.y)])
        for wall in self._room_layout.get_walls():
            intersection = connection_line.intersection(wall)
            if isinstance(intersection, Point):
                return False
        return True
