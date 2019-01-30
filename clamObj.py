import pygame
WHITE = (255, 255, 255)
clamC = pygame.image.load('arts/clamClose.png')
clamE = pygame.image.load('arts/clamEmpty.png')
clamF = pygame.image.load('arts/clamFull.png')
 
class Clam(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    
    def __init__(self, isFull):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        self.image = clamC.convert_alpha()
 
        self.rect = self.image.get_rect()
        self.full = isFull

    def change(self):
        #add sound here
        if self.full:
            self.image = clamF.convert_alpha()
        else:
            self.image = clamE.convert_alpha()
        #self.rect = self.image.get_rect()
