import pygame
from Sprite import Sprite

class Projectile(Sprite, pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (25, 25))

    def update(self):
        self.rect.move_ip(0, -self.speed)
        #check for collision with other sprite
        if