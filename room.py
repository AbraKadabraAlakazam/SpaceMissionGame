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