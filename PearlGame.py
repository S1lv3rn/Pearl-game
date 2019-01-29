import pygame, time, random
from clamObj import Clam


pygame.init()
display_width = 700
display_height = 400

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pearl Game')
clock = pygame.time.Clock()




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

def clam(x,y,img):
    #this puts clams on screen
    gameDisplay.blit(img, (x,y))



def gameLoop():
    #this is the main game gameLoop
    #starts constants, quitting, game display updates


#    x_change = 0
#    thingStartx = random.randrange(0, display_width)
#    thingStarty = -600
#    thingChange = 3
#    thingWidth = 100
#    thingHeight = 100

    sprList = pygame.sprite.Group()
    clam1 = Clam(False)

    clam1.rect.x = (display_width * 0.5)
    clam1.rect.y = (display_height * 0.75)
    sprList.add(clam1)

    money = 0
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                for sprite in sprList:
                   if sprite.rect.collidepoint(pos):
                         print("OPEN")
                         sprite.change()




            print(event)
        gameDisplay.fill(WHITE)

        sprList.update()
        sprList.draw(gameDisplay)
        things_won(money)

        pygame.display.update()


        clock.tick(60)

gameLoop()
pygame.quit()
quit()
