import sys
import pygame
from Player import Player

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

player = Player()
pygame.init()
main = True

#Distance player moves per press
steps = 10
##


while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            main = False


        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                player.control(-steps,0)
            if event.key in [pygame.K_RIGHT, pygame.K_d]:
                player.control(steps,0)

