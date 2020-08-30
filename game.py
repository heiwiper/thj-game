import pygame
from PIL import Image, ImageOps
from first_window import First_window

def draw_map(map1_color, map1, map2):
    im = [
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]
    ]
    for i in range(3):
        for j in range(3):
                if map1_color[i][j] == -1:
                    im[i][j] = Image.open('assets/map/red_'+str(i+1)+str(j+1)+'.png')
                elif map1_color[i][j] == 0:
                    im[i][j] = Image.open('assets/map/original_'+str(i+1)+str(j+1)+'.png')
                else :
                    im[i][j] = Image.open('assets/map/blue_'+str(i+1)+str(j+1)+'.png')

    for i in range(3):
        for j in range(3):
            map1.paste(im[i][j], (187*j, 149*i))

    map2_color = map1_color.copy()
    map2_color.reverse()
    for i in range(3):
        for j in range(3):
                if map2_color[i][j] == -1:
                    im[i][j] = Image.open('assets/map/red_'+str(i+1)+str(j+1)+'.png')
                elif map2_color[i][j] == 0:
                    im[i][j] = Image.open('assets/map/original_'+str(i+1)+str(j+1)+'.png')
                else :
                    im[i][j] = Image.open('assets/map/blue_'+str(i+1)+str(j+1)+'.png')

    for i in range(3):
        for j in range(3):
            map2.paste(im[i][j], (187*j, 149*i))

def display_numbers(number_troops, firstTroopsP1, secondTroopsP1, thirdTroopsP1, firstTroopsP2, secondTroopsP2, thirdTroopsP2):
    font = pygame.font.SysFont('Arial', 40)
    font.set_bold(True)

    remaining_troopsP1 = font.render(str(number_troops-(firstTroopsP1+secondTroopsP1+thirdTroopsP1)), False, (47,60,126))
    remaining_troopsP2 = font.render(str(number_troops-(firstTroopsP2+secondTroopsP2+thirdTroopsP2)), False, (158,15,15))
    firstTroopsP1_text = font.render(str(firstTroopsP1), False, (47,60,126))
    secondTroopsP1_text = font.render(str(secondTroopsP1), False, (47,60,126))
    thirdTroopsP1_text = font.render(str(thirdTroopsP1), False, (47,60,126))
    firstTroopsP2_text = font.render(str(firstTroopsP2), False, (158,15,15))
    secondTroopsP2_text = font.render(str(secondTroopsP2), False, (158,15,15))
    thirdTroopsP2_text = font.render(str(thirdTroopsP2), False, (158,15,15))
    screen.blit(remaining_troopsP1, (35, 780))
    screen.blit(remaining_troopsP2, (685, 780))
    screen.blit(firstTroopsP1_text, (90, 280))
    screen.blit(secondTroopsP1_text, (90+187, 280))
    screen.blit(thirdTroopsP1_text, (90+187*2, 280))
    screen.blit(firstTroopsP2_text, (740, 280))
    screen.blit(secondTroopsP2_text, (740+187, 280))
    screen.blit(thirdTroopsP2_text, (740+187*2, 280))

# display the first window
first_window = First_window()
number_troops = first_window.begin()

# init
pygame.init()
pygame.font.init()

# set the size of the window
size = screenWidth, screenHeight = 1276, 849
screen = pygame.display.set_mode(size)

# set the background of the first window
background = pygame.image.load('assets/background.png')

# set title of the window
pygame.display.set_caption("THJ Game")

#load then play music
# music = pygame.mixer.music.load("./assets/sounds/bgm.wav")
# pygame.mixer.music.play(-1)

map1_color = [
[-1, -1, -1], # red
[0, 0, 0], # original
[1, 1, 1] # blue
]
map1 = Image.new('RGB', (561, 447))
map2 = Image.new('RGB', (561, 447))

firstTroopsP1 = 0
secondTroopsP1 = 0
thirdTroopsP1 = 0
firstTroopsP2 = 0
secondTroopsP2 = 0
thirdTroopsP2 = 0
number_troops_P1 = number_troops_P2 = number_troops
gain1 = 0
gain2 = 0
winner = None
# main loop
run = True
while run:
    screen.blit(background, (0, 0))
    draw_map(map1_color, map1, map2)
    py_map1 =  pygame.image.fromstring(map1.tobytes(), (561, 447), 'RGB')
    py_map2 =  pygame.image.fromstring(map2.tobytes(), (561, 447), 'RGB')
    screen.blit(py_map1, (30, 70))
    screen.blit(py_map2, (680, 70))
    display_numbers(number_troops, firstTroopsP1, secondTroopsP1, thirdTroopsP1, firstTroopsP2, secondTroopsP2, thirdTroopsP2)
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
            if 33<pos[0]<220 and 220<pos[1]<309:
                if event.button == 1 : # LEFT CLICK
                    if(number_troops_P1>0):
                        number_troops_P1-=1
                        firstTroopsP1+=1
                else :
                    if(firstTroopsP1>0):
                        firstTroopsP1-=1
                        number_troops_P1+=1
            elif 220<pos[0]<407 and 220<pos[1]<309:
                if event.button == 1 :
                    if(number_troops_P1>0):
                        number_troops_P1-=1
                        secondTroopsP1+=1
                else :
                    if(secondTroopsP1>0):
                        secondTroopsP1-=1
                        number_troops_P1+=1
            elif 407<pos[0]<594 and 220<pos[1]<309:
                if event.button == 1 :
                    if(number_troops_P1>0):
                        number_troops_P1-=1
                        thirdTroopsP1+=1
                else :
                    if(thirdTroopsP1>0):
                        thirdTroopsP1-=1
                        number_troops_P1+=1
            elif 683<pos[0]<870 and 220<pos[1]<309:
                if event.button == 1 :
                    if(number_troops_P2>0):
                        number_troops_P2-=1
                        firstTroopsP2+=1
                else :
                    if(firstTroopsP2>0):
                        firstTroopsP2-=1
                        number_troops_P2+=1
            elif 870<pos[0]<1057 and 220<pos[1]<309:
                if event.button == 1 :
                    if(number_troops_P2>0):
                        number_troops_P2-=1
                        secondTroopsP2+=1
                else :
                    if(secondTroopsP2>0):
                        secondTroopsP2-=1
                        number_troops_P2+=1
            elif 1057<pos[0]<1244 and 220<pos[1]<309:
                if event.button == 1 :
                    if(number_troops_P2>0):
                        number_troops_P2-=1
                        thirdTroopsP2+=1
                else :
                    if(thirdTroopsP2>0):
                        thirdTroopsP2-=1
                        number_troops_P2+=1
            elif 540<pos[0]<737 and 593<pos[1]<656: # ISSUE DU JEU
                if firstTroopsP1 > firstTroopsP2:
                    gain1+=1
                    gain2-=1
                    map1_color[1][0] = 1
                elif firstTroopsP1 < firstTroopsP2:
                    gain1-=1
                    gain2+=1
                    map1_color[1][0] = -1
                if secondTroopsP1 > secondTroopsP2:
                    gain1+=1
                    gain2-=1
                    map1_color[1][1] = 1
                elif secondTroopsP1 < secondTroopsP2:
                    gain1-=1
                    gain2+=1
                    map1_color[1][1] = -1
                if thirdTroopsP1 > thirdTroopsP2:
                    gain1+=1
                    gain2-=1
                    map1_color[1][2] = 1
                elif thirdTroopsP1 < thirdTroopsP2:
                    gain1-=1
                    gain2+=1
                    map1_color[1][2] = -1
                if gain1 > gain2:
                    winner = pygame.image.load("assets/blueWin.png")
                elif gain1 < gain2:
                    winner =  pygame.image.load("assets/redWin.png")
                else :
                    font = pygame.font.SysFont('Arial', 100)
                    font.set_bold(True)
                    winner = font.render('Match nul !', False, (204,255,153))
