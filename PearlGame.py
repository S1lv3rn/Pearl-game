import pygame, time
from random import randint
from clamObj import Clam


pygame.init()
display_width = 700
display_height = 400

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (62, 114, 165)
RED = (255,0,0)
ORE = (248, 192, 58)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pearl Game')
clock = pygame.time.Clock()





def things_won(count, lf):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Money: " + str(count) + "  Life: " + str(lf), True, ORE)
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
    

def clam(x, y, full, splist):
    #this creates clam objects
    clam = Clam(full)
    clam.rect.x = x
    clam.rect.y = y
    splist.add(clam)
    


def getClamPos(lv, sList):
    #this will num and pos of clams needed, call create clam and return list
    num = 2 + int(lv / 3)

    print("MOD: ",int(lv/3))

    #checking for too many
    if (num*100 + (num-1)*20 > display_width):
        print("ClamNum Execption: ", num, " is too many")
        print("Trying lvl ", lv-1, "\n Recursing....")
        getClamPos(lv-1, sList)
        
    else:
        #get random number
        ran = randint(0,num-1)
        print("RANDINT: ", ran)
        
        #find positions
        for i in range(num):
            y = (display_height * 0.75) - 50
            x = (display_width * ((i+1) / (num+1))) - 50
            print("W: ",display_width,", I: ",i,", F: ",i/(num+1),", SW: ",display_width * (i / (num+1)),", X: ",x)

            print("POS: (",x,",",y,")")
            clam(x, y, i==ran, sList)

def endGame():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Game Over", True, WHITE)
    gameDisplay.blit(text, ((display_height/2), (display_width/2)))


def gameLoop():
    #this is the main game gameLoop
    #starts constants, quitting, game display updates

    lvl = 1
    sprList = pygame.sprite.Group()

    money = 0
    life = 3
    gameExit = False
    alive = True
    getClamPos(lvl, sprList)

    while not gameExit:
        while not alive:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
 
                    for sprite in sprList:
                        if sprite.rect.collidepoint(pos): 
                            print("OPEN")
                            if sprite.open == False:
                                sprite.change()
                             
                                if sprite.full:
                                    money += 1
                                    if (lvl%2 == 0):
                                        life += 1
                                        getClamPos(lvl, sprList)
                                else:
                                    life -= 1
                                    if life == 0:
                                        alive = False
                         
                print(event)
                
            #change bg colour
            gameDisplay.fill(BLUE)
        
            sprList.update()
            sprList.draw(gameDisplay)
            things_won(money, life)
        
            pygame.display.update()
        
            clock.tick(60)

        endGame()

gameLoop()
pygame.quit()
quit()
