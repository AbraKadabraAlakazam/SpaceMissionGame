from pgzero.builtins import *
from gamemap import *
from objects import *
from scenery import *
from player import *
import time

#variabalos

TILE_SIZE = 30

temprow=""

roommap = []

WIDTH = 800
HEIGHT = 600

top_left_x = 100
top_left_y = 150

OBJECT_LIST = objects

room_height = 0
room_width = 0

#Player variabalos
player_x, player_y = 5, 2
oldPlayerX, oldPlayerY = 5,2
playerDirection  = "down"
playerFrame = 0
playerImage = PLAYER[playerDirection][playerFrame]
playerOffsetX, playerOffsetY = 0,0

#Drawing the player
def draw_player():
    playerImage = PLAYER[playerDirection][playerFrame]
    #Calculate tempx
    tempx = top_left_x + player_x * TILE_SIZE + playerOffsetX * TILE_SIZE
    #Calculate tempy
    tempy = top_left_y + player_y * TILE_SIZE + playerOffsetY * TILE_SIZE - playerImage.get_height()
    #draw the player
    screen.blit(playerImage, (tempx, tempy))

#Functions
def draw():
    for y in range(room_height):
        for x in range(room_width):
            item = roommap[y][x]
            if item != 255:


                drawimg = OBJECT_LIST[item][0]

                screen.blit(drawimg, (top_left_x + x*30, top_left_y  + y*30 - drawimg.get_height()))
        if player_y == y:
            draw_player()

def autogen_room():
    global room_map
    global room_number

    height  = GAME_MAP[room_number][1]
    width = GAME_MAP[room_number][2]
    exit_top = GAME_MAP[room_number][3]
    exit_right = GAME_MAP[room_number][4]
    room_map = []

    #check tile
    floor_object = 0
    bottom_edge = 1
    side_edge = 1
    if room_number < 26:
        floor_object  =2
    if room_number in range(1,21):
        bottom_edge=2
        side_edge=2
    if room_number in range(21,26):
        side_edge=2


    #everything else that i forgot to organize
    room_map = []
    temprow = []

    temprow=[side_edge]*width
    room_map.append(temprow)

    for j in range(height-2):
        temprow = []
        temprow.append(side_edge)

        for i in range(width-2):
            temprow.append(floor_object)

        temprow.append(side_edge)
        room_map.append(temprow)

    temprow = []
    temprow = [bottom_edge]*width
    room_map.append(temprow)


    if exit_top:

        room_map[0][int(width/2)] = floor_object

    if exit_right:
    #print(room_map)
        room_map[int(height/2)][width-1] = floor_object

    #inset scenery
    if room_number in scenery:
        for scenery_item in scenery[room_number]:
            scenery_num = scenery_item[0]
            scenery_y = scenery_item[1]
            scenery_x = scenery_item[2]
            room_map[scenery_y][scenery_x] = scenery_num

            image_here = objects[scenery_num][0]
            image_width = image_here.get_width()
            image_width_in_tiles = int(image_width / TILE_SIZE)

            for tile_number in range(1, image_width_in_tiles):
                room_map[scenery_y][scenery_x+tile_number] = 255


    return room_map

def gameloop():
    global player_x, player_y, playerDirection, playerFrame
    global oldPlayerX, oldPlayerY, playerOffsetX, playerOffsetY
    global room_number

    #Before moving, store current pos
    oldPlayerX = player_x
    oldPlayerY = player_y

    if playerFrame == 0:
        if keyboard.right:
            player_x+= 1
            playerDirection = "right"
            playerFrame = 1
        elif keyboard.left:
            player_x -= 1
            playerDirection = "left"
            playerFrame = 1
        elif keyboard.up:
            player_y -=1
            playerDirection = "up"
            playerFrame = 1
        elif keyboard.down:
            player_y +=1
            playerDirection = "down"
            playerFrame = 1

    if playerFrame > 0:
        playerFrame +=1
        time.sleep(0.05)
        #Adjut the offsets
        if playerDirection == "right":
            playerOffsetX = -1 + 0.25 * playerFrame
        elif playerDirection == "left":
            playerOffsetX = 1 - 0.25 * playerFrame
        elif playerDirection == "up":
            playerOffsetY = 1 - 0.25 * playerFrame
        elif playerDirection == "down":
            playerOffsetY = -1 + 0.25 * playerFrame
        # loop back around to frame zero when needed
        if playerFrame == 5:
            playerFrame = 0
            playerOffsetX = 0
            playerOffsetY = 0

    #Check for exitng the room_height
    if player_x == room_width: #door on the RIIIIGIITHHt
        room_number += 1
        autogen_room()
        player_x = 0 #enter at the left
        player_y = int(room_height/2)
        playerFrame = 0
        return
        #START HERE MEXT WEEK



    #Dont walk throught things
    if room_map[player_y][player_x] not in items_player_may_stand_on:
        player_x = oldPlayerX
        player_y = oldPlayerY


clock.schedule_interval(gameloop, 0.03)


#Making the map
room_number = 31

roommap = autogen_room()