from collections import defaultdict
from dataclasses import dataclass
from shapely.geometry import LineString
from tkinter import *
import pygame
from src.room_layout import RoomLayout

from src.user_position_storage import UserPositionStorage


@dataclass
class UserDrawingSettings:
    user_color = (166, 166, 0)


class Display:
    def __init__(self, users: UserPositionStorage, map: RoomLayout) -> None:
        self.user_settings = UserDrawingSettings()
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.map = map
        self.users = users
        self.is_running = True

    def update(self) -> None:
        self.screen.fill("black")
        for user in self.users.get_users():
            pygame.draw.circle(surface=self.screen,
                               color=self.user_settings.user_color,
                               center=(user.position.x, user.position.y),
                               )
        pygame.display.flip()
        self.delta_time = self.clock.tick(0.5)

    def run(self) -> None:
        while self.is_running:
            self.check_events()
            self.update()

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
