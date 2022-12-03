from math import floor

from shapely.geometry import LineString, Point


class RoomLayout:
    def __init__(self) -> None:
        self._walls: list[LineString] = []

    def get_walls(self) -> list[LineString]:
        return self._walls

    def process_room_layout(self, layout: list[int], room_size: int) -> None:
        def calculate_coordinate_from_index(index: int) -> list[int, int]:
            return [floor(index / room_size), index % room_size]

        for idx, section in enumerate(layout):
            if section == 1:
                try:
                    if idx % room_size != room_size - 1:
                        if layout[idx + 1] == 1:
                            self._walls.append(LineString([calculate_coordinate_from_index(idx),
                                                           calculate_coordinate_from_index(idx + 1)]))
                except IndexError:
                    pass
                try:
                    if layout[idx + room_size] == 1:
                        self._walls.append(LineString([calculate_coordinate_from_index(idx),
                                                       calculate_coordinate_from_index(idx + room_size)]))
                except IndexError:
                    pass
