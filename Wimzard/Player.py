import pygame.sprite
from Constants import *

MAX_X = WIDTH
MAX_Y = HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def control(self,x,y):
        self.x += x
        self.y += y

    def getPosition(self):
        # calculate the position of the sprite
        return self.x, self.y

    def goUp(self, move=1):
        self.y -= move
    def goDown(self, move=1):
        self.y += move
    def goLeft(self, move=1):
        self.x -= move
    def goRight(self, move=1):
        self.x += move

    def update(self, keypressed):
        if keypressed[pygame.K_LEFT]:
            #if the pressed key is left execute the left function
            self.goLeft()
        if keypressed[pygame.K_RIGHT]:
            self.goRight()
        if keypressed[pygame.K_UP]:
            self.goUp()
        if keypressed[pygame.K_DOWN]:
            self.goDown()
        if keypressed[pygame.K_SPACE]:
            pass
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