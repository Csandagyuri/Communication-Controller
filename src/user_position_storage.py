from copy import deepcopy
from typing import Protocol

from src.user import User


class UserPositionStorage(Protocol):
    def update_position(self, user: User) -> None:
        pass

    def get_users_except(self, user: User) -> list[User]:
        pass

    def get_users(self) -> list[User]:
        pass


class InMemoryUserPositionStorage(UserPositionStorage):
    def __init__(self) -> None:
        self._users: list[User] = []

    def update_position(self, user: User) -> None:
        if user in self._users:
            self._users.remove(user)
        self._users.append(user)

    def get_users_except(self, user: User) -> list[User]:
        users = deepcopy(self._users)
        if user in users:
            users.remove(user)
        return users

    def get_users(self) -> list[User]:
        return deepcopy(self._users)