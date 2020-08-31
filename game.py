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
    font = pygame.font.SysFont('Arial', 40)
    font.set_bold(True)

    remaining_troopsP1 = font.render(str(number_troops-(player1Troops[0]+player1Troops[1]+player1Troops[2])), False, (47,60,126))
    remaining_troopsP2 = font.render(str(number_troops-(player2Troops[0]+player2Troops[1]+player2Troops[2])), False, (158,15,15))
    player1TroopsText = []
    player2TroopsText = []
    for n in range(number_troops):
        player1TroopsText.append(font.render(str(player1Troops[n]), False, (158,15,15)))
        player2TroopsText.append(font.render(str(player2Troops[n]), False, (47,60,126)))

    screen.blit(remaining_troopsP1, (35, 780))
    screen.blit(remaining_troopsP2, (685, 780))
    for i in range(number_troops):
        screen.blit(player1TroopsText[i], (60, 140+230*i))
        screen.blit(player2TroopsText[i], (width-80, 140+230*i))

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


# init
pygame.init()
pygame.font.init()

# set the size of the window
size = screenWidth, screenHeight = width, height
screen = pygame.display.set_mode(size)

# set the background of the first window
background = pygame.image.load('assets/background.png')
mapImage = pygame.image.load('assets/map/full_map.png')

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
    screen.blit(background, (0, 0))
    draw_map(mapColors, map)
    py_map =  pygame.image.fromstring(map.tobytes(), (1015, 690), 'RGBA')
    screen.blit(mapImage, (132, 30))
    screen.blit(py_map, (132, 30))
    display_numbers(number_troops, player1Troops, player2Troops)
    if winner!=None :
        if gain1 == gain2:
            screen.blit(winner, (420, 250))
        else :
            screen.blit(winner, (500, 180))
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
                    winner = pygame.image.load("assets/blueWin.png")
                elif gain1 < gain2:
                    winner =  pygame.image.load("assets/redWin.png")
                else:
                    font = pygame.font.SysFont('Arial', 100)
                    font.set_bold(True)
                    winner = font.render('Match nul !', False, (204,255,153))
