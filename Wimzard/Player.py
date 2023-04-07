import pygame.sprite
from Constants import *
from Sprite import Sprite
from Projectile import Projectile


class Player(pygame.sprite.Sprite, Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.x = 600
        self.y = 500
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

#im not even sure if we use this method anywhere
    def control(self,x,y):
        self.x += x
        self.y += y

# makes the player move left and right during the mainloop
    def update(self, keypressed):
        if keypressed[pygame.K_LEFT]:
            #if the pressed key is left execute the left function
            self.goLeft()
        if keypressed[pygame.K_RIGHT]:
            self.goRight()


