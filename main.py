from operator import iconcat

import pygame
from pygame.display import set_allow_screensaver

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode(SCREEN_WIDTH,SCREEN_HEIGHT)
pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("screns/oppo.jpg")
running = True
while running:
    pass

pygame.quit()