
class CommunicationController:
    def __init__(self, user_position_storage: UserPositionStorage, connection_ruler: ConnectionRuler) -> None:
        self._user_position_storage = user_position_storage
        self.user_connections: dict[user_id, Operation] = {}
        self._connection_ruler = connection_ruler

    def process(self, user_id: str, position: Position) -> list[Operation]:
        self._user_position_storage.update_position(user_id)
        needed_connections: list[Connection]  = self._calculate_needed_connections(user_id)
        operations: list[Operation] = self._calculate_operations(user_id, needed_connections)
        self._apply_operations(operations)
        return operations

    def _calculate_needed_connections(self, user_id: str) -> list[Connection]:
        return [connection := self._connection_ruler.get_connection_type(client= user_id,
                                                                        communication_partner=user)
                for user in self._user_position_storage.get_users_except(user_id)
                if connection is not None]

    def _calculate_operations(self, user_id: str, needed_connections: list[Connection]) -> list[Operation]:
        result: list[Connection] = []
        for needed_connection in needed_connections:
            if needed_connection not in self.user_connections[user_id]:
                result.append(LeaveOperation(needed_connection))
        for user_connection in self.user_connections[user_id]:
            if user_connection not in needed_connections:
                result.append(JoinOperation(user_connection))
        return result