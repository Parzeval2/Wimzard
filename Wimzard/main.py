import sys
import pygame
from Player import Player
from Constants import *
from Enemy import Enemy
from Projectile import Projectile

screen = pygame.display.set_mode((WIDTH, HEIGHT))
enemy = Enemy("spider.png")
player = Player("wizard.png")

main = True

enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(enemy)

projectile_group = pygame.sprite.GroupSingle()
while main:
    pygame.init()

    # get player input
    keys = pygame.key.get_pressed()
    # player exits game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # projectile handling
    if keys[pygame.K_SPACE]:
        projectile = Projectile("Fireball.png")
        projectile.rect.midbottom = player.rect.midtop
        projectile_group.add(projectile)


    # player movement check
    player.update(keys)

    # make background
    screen.fill(WHITE)
    # update sprites
    if not enemy.alive:
        enemy = Enemy("spider.png")
        enemy_sprites.add(enemy)
    # enemy sprite
    enemy_sprites.update()
    #projectile sprites
    projectile_group.update(enemy_sprites)

    # draw sprites on the screen
    enemy_sprites.draw(screen)
    projectile_group.draw(screen)
    screen.blit(player.image, player.getPosition())
    # load screen
    pygame.display.flip()
