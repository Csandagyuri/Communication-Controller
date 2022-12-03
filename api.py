from collections import defaultdict

from fastapi import FastAPI
from src.communication_controller import CommunicationController
from src.connection_ruler import ConnectionBasedOnRange
from src.connection_storage import ConnectionStorage

from src.operation import Operation
from src.position import Position
from src.room_layout import RoomLayout
from src.user import User
from src.user_position_storage import InMemoryUserPositionStorage

app = FastAPI()
user_position_storage = InMemoryUserPositionStorage()
room_layout = RoomLayout()
room_layout.process_room_layout(
            [1,1,1,1,1,1,1,1,
             1,0,1,0,0,0,0,1,
             1,1,0,1,1,1,1,1,
             1,0,0,0,0,1,0,1,
             1,0,1,0,0,1,0,1,
             1,0,1,0,0,1,0,1,
             1,1,1,1,1,1,0,1,
             1,0,0,0,0,1,0,1,
             1,0,0,0,0,0,0,1,
             1,1,1,1,1,1,1,1,], 8)
connections= ConnectionStorage()

controller = CommunicationController(
    user_position_storage=user_position_storage,
    connection_ruler=ConnectionBasedOnRange(
        socket_range=2.0,
        nakama_range=5.0,
        room_layout=room_layout
    ),
    user_connections=connections,
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/user/{user_id}")
async def send_data(user_id: str, socket_id: str, position: Position):
    operations: list[Operation] = controller.process(User(id=user_id,
                                                          socket_id=socket_id,
                                                          position=position))
    return operations


@app.get("/users")
async def get_users():
    return user_position_storage.get_users()


@app.get("/connections")
async def get_connections():
    return connections

