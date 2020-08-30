import pygame
import random
class First_window :
    def __init__(self):
        pass

    def begin(self):
        pygame.init()
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 40)
        font.set_bold(True)
        size = screenWidth, screenHeight = 864, 317

        #set size of the window
        screen = pygame.display.set_mode(size)

        # set the background of the first window
        background = pygame.image.load('assets/first_window.png')

        # set title of the window
        pygame.display.set_caption("THJ Game")

        # number of troops
        number_troops = 3

        # first window loop
        begin_game = False
        while not begin_game:
            screen.blit(background, (0, 0))
            text = font.render(str(number_troops), False, (47,60,126))
            screen.blit(text, (420, 140))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        return number_troops
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 489<pos[0]<499 and 153<pos[1]<171:
                        if(number_troops<24):
                            number_troops+=1
                    elif 504<pos[0]<514 and 153<pos[1]<171:
                        if(number_troops>3):
                            number_troops-=1
