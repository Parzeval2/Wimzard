import pygame.sprite


class Player:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0

    def control(self,x,y):
        self.x += x
        self.y += y

    def update(self):
        self.rect.x = self.rect.x + self.x
        self.rect.y = self.rect.y + self.y