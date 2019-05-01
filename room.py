from gamemap import

def autogen_room(height, width, exit_top, exit_right):
    room_map = []
    temprow = []

    temprow=[1]*width
    room_map.append(temprow)

    for j in range(height-2):
        temprow = []
        temprow.append(1)

        for i in range(width-2):
            temprow.append(0)

        temprow.append(1)
        room_map.append(temprow)

    temprow = []
    temprow = [1]*width
    room_map.append(temprow)

    if exit_top:

        room_map[0][int(width/2)] = 0

    if exit_right:
        print(room_map)
        room_map[int(height/2)][width-1] = 0

    return room_map

#TEST
room = autogen_room(7,18, True, True)
print(room)
temprow=""

for row in range(len(room)):
    for col in range(len(room[row])):
        temprow = temprow + str(room[row][col])
    print(temprow)
    temprow=""

room = [
[1,1,1,1,1],
[1,0,0,0,1],
[1,0,1,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,0,0,0,1],
[1,1,1,1,1]
]

WIDTH = 800
HEIGHT = 600

top_left_x = 100
top_left_y = 150

OBJECT_LIST = [images.floor, images.pillar]

room_height = 7
room_width = 5

def draw():
    for y in range(room_height):
        for x in range(room_width):
            item = room[y][x]

            drawimg = OBJECT_LIST[item]

            screen.blit(drawimg, (top_left_x + x*30, top_left_y  + y*30 - drawimg.get_height()))