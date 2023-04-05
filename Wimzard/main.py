import sys
import pygame
from Player import Player
from Constants import *
from Enemy import Enemy

screen = pygame.display.set_mode((WIDTH, HEIGHT))
enemy = Enemy("spider.png")
player = Player("wizard.png")
pygame.init()
main = True

#Distance player moves per press
steps = 10
##


while main:

    #get player input
    keys = pygame.key.get_pressed()
    #player exits game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #player movement check
    player.update(keys)

    #make background
    screen.fill(WHITE)

    #spawn player sprite
    screen.blit(player.image, player.getPosition())
    #load screen
    pygame.display.flip()

    #start the enemy spawning and moving


