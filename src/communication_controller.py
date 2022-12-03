
from src.connection_ruler import ConnectionRuler
from src.connection_storage import ConnectionStorage
from src.operation import Operation, OperationFactory
from src.user import User
from src.user_position_storage import UserPositionStorage
from src.connection import Connection


class CommunicationController:
    def __init__(
            self, user_position_storage: UserPositionStorage,
            connection_ruler: ConnectionRuler,
            user_connections: ConnectionStorage
    ) -> None:
        self._user_position_storage = user_position_storage
        self._connection_ruler = connection_ruler
        self._user_connections = user_connections

    def process(self, user: User) -> list[Operation]:
        self._user_position_storage.update_position(user)
        needed_connections: list[Connection] = self._calculate_needed_connections(user)
        operations: list[Operation] = self._calculate_operations(user, needed_connections)
        return operations

    def _calculate_needed_connections(self, user: User) -> list[Connection]:
        result = []
        for partner in self._user_position_storage.get_users_except(user):
            connection = self._connection_ruler.get_connection_type(client=user, communication_partner=partner)
            if connection is not None:
                result.append(connection)
        return result

    def _calculate_operations(self, user: User, needed_connections: list[Connection]) -> list[Operation]:
        result: list[Operation] = []
        for needed_connection in needed_connections:
            if needed_connection not in self._user_connections[user.id]:
                result.append(OperationFactory.create_join_operation(needed_connection))
                self._user_connections[user.id].append(needed_connection)
        for user_connection in self._user_connections[user.id]:
            if user_connection not in needed_connections:
                result.append(OperationFactory.create_leave_operation(user_connection))
                self._user_connections[user.id].remove(user_connection)
        return result
