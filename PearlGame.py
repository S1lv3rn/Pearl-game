import pygame
import time
import random

pygame.init()
display_width = 800
display_height = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('arts/car.png')
car_width = 85
