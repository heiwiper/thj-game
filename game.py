import pygame
from PIL import Image, ImageOps

from first_window import First_window

width = 1280
height =960
mapColumns = 7
mapRows = 3


def draw_map(mapColors, map):
    imageMap = []
    for r in range(mapRows):
        tempList = []
        for c in range(mapColumns):
            tempList.append(None)
        imageMap.append(tempList)

    for r in range(mapRows):
        for c in range(mapColumns):
            if mapColors[r][c] == 1:
                imageMap[r][c] = Image.open('assets/map/red_rect.png')
            elif mapColors[r][c] == -1:
                imageMap[r][c] = Image.open('assets/map/blue_rect.png')
            else:
                imageMap[r][c] = Image.open('assets/map/frontier.png')

    for r in range(mapRows):
        for c in range(mapColumns):
            map.paste(imageMap[r][c], (145*c, 230*r))


def display_numbers(number_troops, player1Troops, player2Troops):
    font = pygame.font.SysFont('Arial', 28)
    font.set_bold(False)

    remaining_troopsP1 = font.render(str(number_troops-(player1Troops[0]+player1Troops[1]+player1Troops[2])), False, (255,255,255))
    remaining_troopsP2 = font.render(str(number_troops-(player2Troops[0]+player2Troops[1]+player2Troops[2])), False, (255,255,255))

    font = pygame.font.SysFont('Arial', 40)
    font.set_bold(True)
    player1TroopsText = []
    player2TroopsText = []
    for i in range(mapRows):
        player1TroopsText.append(font.render(str(player1Troops[i]), False, (158,15,15)))
        player2TroopsText.append(font.render(str(player2Troops[i]), False, (47,60,126)))

    image_rect = blueHelmet.get_rect()
    image_rect.center = (132/2+width-132, (height-880)/2+890)
    screen.blit(blueHelmet, image_rect)

    image_rect = redHelmet.get_rect()
    image_rect.center = (132/2, (height-880)/2+890)
    screen.blit(redHelmet, image_rect)

    text_rect = player1TroopsText[i].get_rect(center=(146/2, 910))
    screen.blit(remaining_troopsP1, text_rect)
    text_rect = player2TroopsText[i].get_rect(center=(132/2+width-132, 910))
    screen.blit(remaining_troopsP2, text_rect)
    image_rect = shieldImage.get_rect()
    for i in range(mapRows):
        image_rect.center = (132/2, 230/2+230*i+30)
        screen.blit(shieldImage, image_rect)
        text_rect = player1TroopsText[i].get_rect(center=(132/2, 230/2+230*i+30))
        screen.blit(player1TroopsText[i], text_rect)

        image_rect.center = (132/2+width-132, 230/2+230*i+30)
        screen.blit(shieldImage, image_rect)
        text_rect = player2TroopsText[i].get_rect(center=(132/2+width-132, 230/2+230*i+30))
        screen.blit(player2TroopsText[i], text_rect)

# display the first window
first_window = First_window()
number_troops = first_window.begin()


def claim_territory(player, row):
    for c in range(mapColumns):
        if mapColors[row][c] == 0:
            if player == 1:
                mapColors[row][c] = 1
                if c != mapColumns-1:
                    mapColors[row][c+1] = 0
                return
            elif player == 2:
                mapColors[row][c] = -1
                if c != 0:
                    mapColors[row][c-1] = 0
                return

frameCount = 0
player1Sprites = []
player2Sprites = []
statesList = ["standing", "won", "lost"]
for sprites in statesList:
    tempList1 = []
    tempList2 = []
    for c in range(2):
        tempList1.append(pygame.image.load('./assets/characters/red/{}_{}.png'.format(sprites, c)))
        tempList2.append(pygame.image.load('./assets/characters/blue/{}_{}.png'.format(sprites, c)))
    player1Sprites.append(tempList1)
    player2Sprites.append(tempList2)

def draw_players(state1, state2, frameCount):
    if frameCount >= 2:
        frameCount = 0
    maxFrames = 0
    if state1 == "standing" or state1 == "won":
        maxFrames = 2
    elif state1 == "lost":
        maxFrames = 1

    statePlayer1 = statesList.index(state1)
    statePlayer2 = statesList.index(state2)
    screen.blit(player1Sprites[statePlayer1][frameCount], (10, 880-player1Sprites[statePlayer1][frameCount].get_rect().height))
    screen.blit(player2Sprites[statePlayer2][frameCount], (width-player2Sprites[statePlayer2][frameCount].get_rect().width-10, 880-player2Sprites[statePlayer2][frameCount].get_rect().height))
    return frameCount+1


def redraw_game_window(frameCount):
    screen.blit(background, (0, 0))
    draw_map(mapColors, map)
    py_map =  pygame.image.fromstring(map.tobytes(), (1015, 690), 'RGBA')
    screen.blit(mapImage, (132, 30))
    screen.blit(py_map, (132, 30))
    display_numbers(number_troops, player1Troops, player2Troops)
    frameCount = draw_players(player1State, player2State, frameCount)
    if winner is not None:
        if gain1 == gain2:
            screen.blit(winner, (420, 250))
        else :
            screen.blit(winner, (500, 180))
    return frameCount

# init
pygame.init()
pygame.font.init()

# set the size of the window
size = screenWidth, screenHeight = width, height
screen = pygame.display.set_mode(size)

# set the background of the first window
background = pygame.image.load('assets/background.png')
mapImage = pygame.image.load('assets/map/full_map.png')

blueHelmet = pygame.image.load('assets/characters/blue/blue_helmet.png')
redHelmet = pygame.image.load('assets/characters/red/red_helmet.png')
shieldImage = pygame.image.load('assets/shield.png')

# set title of the window
pygame.display.set_caption("THJ Game")

#load then play music
# music = pygame.mixer.music.load("./assets/sounds/bgm.wav")
# pygame.mixer.music.play(-1)

mapColors = []
for r in range(mapRows):
    tempList = []
    for c in range(mapColumns):
        if c < mapColumns//2:
            tempList.append(1)
        elif c == mapColumns//2:
            tempList.append(0)
        else:
            tempList.append(-1)
    mapColors.append(tempList)

map = Image.new('RGBA', (1015, 690))

player1State = "standing"
player2State = "standing"
player1Troops = []
player2Troops = []
for i in range(mapRows):
    player1Troops.append(0)
    player2Troops.append(0)
numberTroopsP1 = numberTroopsP2 = number_troops
gain1 = 0
gain2 = 0
winner = None

# main loop
run = True
while run:
    frameCount = redraw_game_window(frameCount)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 0<pos[0]<132 and 30<pos[1]<260:
                if event.button == 1 : # LEFT CLICK
                    if(numberTroopsP1>0):
                        numberTroopsP1-=1
                        player1Troops[0]+=1
                else :
                    if(player1Troops[0]>0):
                        player1Troops[0]-=1
                        numberTroopsP1+=1
            elif 0<pos[0]<132 and 260<pos[1]<490:
                if event.button == 1 :
                    if(numberTroopsP1>0):
                        numberTroopsP1-=1
                        player1Troops[1]+=1
                else :
                    if(player1Troops[1]>0):
                        player1Troops[1]-=1
                        numberTroopsP1+=1
            elif 0<pos[0]<132 and 490<pos[1]<720:
                if event.button == 1 :
                    if(numberTroopsP1>0):
                        numberTroopsP1-=1
                        player1Troops[2]+=1
                else :
                    if(player1Troops[2]>0):
                        player1Troops[2]-=1
                        numberTroopsP1+=1
            elif 1148<pos[0]<width and 30<pos[1]<260:
                if event.button == 1 :
                    if(numberTroopsP2>0):
                        numberTroopsP2-=1
                        player2Troops[0]+=1
                else :
                    if(player2Troops[0]>0):
                        player2Troops[0]-=1
                        numberTroopsP2+=1
            elif 1148<pos[0]<width and 260<pos[1]<490:
                if event.button == 1 :
                    if(numberTroopsP2>0):
                        numberTroopsP2-=1
                        player2Troops[1]+=1
                else :
                    if(player2Troops[1]>0):
                        player2Troops[1]-=1
                        numberTroopsP2+=1
            elif 1148<pos[0]<width and 490<pos[1]<720:
                if event.button == 1 :
                    if(numberTroopsP2>0):
                        numberTroopsP2-=1
                        player2Troops[2]+=1
                else :
                    if(player2Troops[2]>0):
                        player2Troops[2]-=1
                        numberTroopsP2+=1
            elif 540<pos[0]<737 and 593<pos[1]<656: # ISSUE DU JEU
                if player1Troops[0] > player2Troops[0]:
                    gain1+=1
                    gain2-=1
                    claim_territory(1, 0)
                elif player1Troops[0] < player2Troops[0]:
                    gain1-=1
                    gain2+=1
                    claim_territory(2, 0)
                if player1Troops[1] > player2Troops[1]:
                    gain1+=1
                    gain2-=1
                    claim_territory(1, 1)
                elif player1Troops[1] < player2Troops[1]:
                    gain1-=1
                    gain2+=1
                    claim_territory(2, 1)
                if player1Troops[2] > player2Troops[2]:
                    gain1+=1
                    gain2-=1
                    claim_territory(1, 2)
                elif player1Troops[2] < player2Troops[2]:
                    gain1-=1
                    gain2+=1
                    claim_territory(2, 2)
                if gain1 > gain2:
                    winner = pygame.image.load("assets/redWin.png")
                    player1State = "won"
                    player2State = "lost"
                elif gain1 < gain2:
                    winner = pygame.image.load("assets/blueWin.png")
                    player1State = "lost"
                    player2State = "won"
                else:
                    font = pygame.font.SysFont('Arial', 100)
                    font.set_bold(True)
                    winner = font.render('Match nul !', False, (204,255,153))
                    player1State = "lost"
                    player2State = "lost"
