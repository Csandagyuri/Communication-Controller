from pydantic import BaseModel

class Operation(BaseModel):
    op_code: int
    target_type: str
    target_id: str
