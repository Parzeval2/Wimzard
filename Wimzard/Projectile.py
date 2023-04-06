import pygame.sprite
from Sprite import Sprite

class Projectile(pygame.sprite.Sprite, Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.speed = 1


    def update(self):
        #move up
        self.rect.move_ip(0, -self.speed)