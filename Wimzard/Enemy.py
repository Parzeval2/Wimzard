from random import random, randint
from Sprite import Sprite
import pygame.sprite
from Constants import *
import time

MAX_X = WIDTH
MAX_Y = HEIGHT

class Enemy(pygame.sprite.Sprite, Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(img)
        self.speed = 50
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        #for if the spider is moving and alive
        self.next_move_time = time.monotonic()
        self.alive = True

    #choose random movement action
    def randomMovement(self):
        # choose a random direction to move
        choice = randint(1, 16)
        if choice in [1, 4, 5]:
            self.rect.move_ip(0, self.speed)  # move down
        elif choice in [2, 6,13]:
            #move up
            self.rect.move_ip(0, -self.speed)
        elif choice in [3, 7, 8, 9, 10,11,12,14,15]:
            self.rect.move_ip(self.speed, 0)  # move right

        # make sure the enemy stays within the screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        #is enemy on screen?
        if self.rect.x > WIDTH:
            self.alive = False

    def update(self):
        # check if it's time to move the enemy
        if self.alive:
            if time.monotonic() >= self.next_move_time:
                self.randomMovement()
                self.next_move_time = time.monotonic() + 0.3  # move every second
        else:
            #if the enemy is dead we just reset the entity basically
            self.kill()
            self.alive = False


