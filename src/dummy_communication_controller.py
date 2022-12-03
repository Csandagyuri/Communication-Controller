
from src.operation import Operation
from src.position import Position


class DummyCommunicationController:
    def process(self, user_id: str, position: Position) -> list[Operation]:
        return [Operation(op_code=1, target_type="nakama", target_id= "08e93940-280c-4ecd-a867-3f44dd7a344b.nakama1")]