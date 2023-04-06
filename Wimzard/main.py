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

projectile_group = pygame.sprite.Group()

MAX_PROJECTILES = 1
projectile_count = 0
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
        if projectile_count < MAX_PROJECTILES:
            projectile = Projectile("Fireball.png")
            projectile.rect.x = player.x
            projectile.rect.y = player.y
            projectile_group.add(projectile)
            projectile_count += 1
        else:
            pass

    #collision handling for the projectile and enemy group
    for projectile in projectile_group:
        for enemy in enemy_sprites:
            if projectile.rect.colliderect(enemy.rect):
                print("enemy hit")
                projectile.kill()
                enemy.alive = False
                enemy.kill()
                projectile_count -= 1
    #checking for the projectile being off screen
    for projectile in projectile_group:
        if projectile.rect.y < 0:
            projectile.kill()
            projectile_group.remove(projectile)
            projectile_count -= 1

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
    projectile_group.update()

    # draw sprites on the screen
    enemy_sprites.draw(screen)
    projectile_group.draw(screen)
    screen.blit(player.image, player.getPosition())
    # load screen
    pygame.display.flip()
