
#from src.communication_controller import CommunicationController
from src.operation import Operation
from src.position import Position


class DummyCommunicationController():
    def process(self, user_id: str, position: Position) -> list[Operation]:
        return [Operation(op_code=1, target_type="socket", target_id= "ws://127.0.0.1:7890/Echo")]