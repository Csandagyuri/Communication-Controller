from pydantic import BaseModel
from src.connection import Connection


class Operation(BaseModel):
    op_code: int
    target_type: str
    target_id: str


class OperationFactory:
    @staticmethod
    def create_join_operation(connection: Connection):
        return Operation(op_code=1, target_type=connection.type, target_id=connection.address)

    @staticmethod
    def create_leave_operation(connection: Connection):
        return Operation(op_code=2, target_type=connection.type, target_id=connection.address)