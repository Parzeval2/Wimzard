import sys
import pygame
from Player import Player
from Constants import *
from Enemy import Enemy
from random import randint
import time

screen = pygame.display.set_mode((WIDTH, HEIGHT))
enemy = Enemy("spider.png")
player = Player("wizard.png")

main = True

enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(enemy)


while main:
    pygame.init()

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
    #update sprites
    #enemy sprite
    enemy_sprites.update()
    #draw sprites on the screen
    enemy_sprites.draw(screen)
    screen.blit(player.image, player.getPosition())
    #load screen
    pygame.display.flip()




