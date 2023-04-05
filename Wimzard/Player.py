import pygame.sprite
from Constants import *
from Sprite import Sprite


class Player(pygame.sprite.Sprite, Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = 600
        self.y = 500
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

    def control(self,x,y):
        self.x += x
        self.y += y


    def update(self, keypressed):
        if keypressed[pygame.K_LEFT]:
            #if the pressed key is left execute the left function
            self.goLeft()
        if keypressed[pygame.K_RIGHT]:
            self.goRight()
        # if keypressed[pygame.K_UP]:
        #     self.goUp()
        # if keypressed[pygame.K_DOWN]:
        #     self.goDown()
        if keypressed[pygame.K_SPACE]:
            pass