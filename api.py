from fastapi import FastAPI

from src.operation import Operation
from src.position import Position
from src.dummy_communication_controller import DummyCommunicationController

app = FastAPI()
controller = DummyCommunicationController()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/user/{user_id}")
async def send_data(user_id: int, position: Position):
    operations: list[Operation] = controller.process(user_id, Position(x=0,y=0,z=0))
    return operations
