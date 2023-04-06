import pygame
from Sprite import Sprite

class Projectile(Sprite, pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.speed = 10


    def update(self,other):
        self.rect.move_ip(0, -self.speed)
        #check for collision with other sprite
        enemies_hit = pygame.sprite.spritecollide(self, other, True)
        if enemies_hit:
            self.kill()