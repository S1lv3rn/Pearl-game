import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

#clam coords


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pearl Game')
clock = pygame.time.Clock()
clamC = pygame.image.load('arts/clamClose.png')
clamE = pygame.image.load('arts/clamEmpty.png')
clamF = pygame.image.load('arts/clamFull.png')

#car_width = 85

#def checkClam():
    #this method will check the


def things_won(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Money: " + str(count), True, BLACK)
    gameDisplay.blit(text, (0,0))

def textObjects(text, font):
    #related to messageDisplay
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def messageDisplay(text):
    #this method displays the given text on screen
    largeTxt = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = textObjects(text, largeTxt)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    gameLoop()

def clam(x,y):
    #this puts clams on screen
    gameDisplay.blit(clamC, (x,y))



def gameLoop():
    #this is the main game gameLoop
    #starts constants, quitting, game display updates
    x1 = (display_width * 0.25) #coords for player
    x2 = (display_width * 0.5)
    x3 = (display_width * 0.75)

    xArr = [x1, x2, x3]

    y = (display_height * 0.8)
#    x_change = 0
#    thingStartx = random.randrange(0, display_width)
#    thingStarty = -600
#    thingChange = 3
#    thingWidth = 100
#    thingHeight = 100

    money = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #x_change = -5
                elif event.key == pygame.K_RIGHT:
                    #x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #x_change = 0

            print(event)


        gameDisplay.fill(WHITE)
        for x in xArr:
            car(x,y)

        things_won(money)


        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
quit()
