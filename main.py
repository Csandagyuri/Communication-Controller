from src.room_layout import RoomLayout


def main():
    room_layout_list=[0,0,0,0,0,
                      0,1,1,1,0,
                      0,1,0,1,0,
                      0,1,1,1,0,
                      0,0,0,0,0,]
    room_size = 5
    room_layout = RoomLayout()
    room_layout.process_room_layout(layout=room_layout_list, room_size=room_size)

    for wall in room_layout.get_walls():
        first, last = wall.boundary
        print(f'first{first}')
        print(f'second{last}')


if __name__ == '__main__':
    main()