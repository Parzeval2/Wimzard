from random import random, randint

import pygame.sprite
from Constants import *

MAX_X = WIDTH
MAX_Y = HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()


    def getPosition(self):
        # calculate the position of the sprite
        return self.x, self.y

    def goDown(self, move=1):
        self.y += move
    def goLeft(self, move=1):
        self.x -= move
    def goRight(self, move=1):
        self.x += move

    #choose random movement action
    def randomMovement(self):
        choice = randint(1,3)
        if choice == 1:
            self.goDown()
        if choice == 2:
            self.goLeft()
        if choice == 3:
            self.goRight()
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        # checks for x being larger than the max or smaller than 0
        if x > MAX_X:
            self._x = MAX_X
        elif x <= 0:
            self._x = 0
        else:
            self._x = x

    # y accessor and mutator
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        # checks for y being larger than the max or smaller than 0
        if y > MAX_Y:
            self._y = MAX_Y
        elif y <= 0:
            self._y = 0
        else:
            self._y = y