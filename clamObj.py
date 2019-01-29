import pygame
WHITE = (255, 255, 255)
clamC = pygame.image.load('arts/clamClose.png')
clamE = pygame.image.load('arts/clamEmpty.png')
clamF = pygame.image.load('arts/clamFull.png')

class Clam(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.


    def __init__(self, isFull):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = clamC

        self.rect = self.image.get_rect()
        self.full = isFull

    def change(self):
        #add sound here
        if self.full:
            self.image = clamF
        else:
            self.image = clamE
        
