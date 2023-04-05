#####################################################################
# author:   
# date:    
# description: 
#####################################################################
import pygame
from random import randint, choice
from Item import Item
from Constants import *


class Person(pygame.sprite.Sprite, Item):
    def __init__(self):
        #Have to import the initializer of the parent class
        Item.__init__(self)
        #start the screen as white and make it hex
        self.color = [255, 255, 255]
        self.surf = pygame.Surface((WIDTH, HEIGHT))
        self.surf.fill(self.color)
        #start the cube in the center of the screen
        self.x = WIDTH/2
        self.y = HEIGHT/2

    #for setcolor, use random choice
    def setColor(self):
        random_color = choice(COLORS)
        self.color = random_color
        self.surf.fill(self.color)

    def setSize(self):
        self.size = randint(4,100)
        #just creates a new surface and garbage collector takes care of old one
        self.surf = pygame.Surface((self.size, self.size))
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
            #changes color and size randomly
            self.setSize()
            self.setColor()
    def setRandomPos(self):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)

    def getPosition(self):
        #calculate the position of the person
        x = self.x - self.size/2
        y = self.y - self.size/2
        return (x, y)

    def __str__(self):
        return f"Person({self.name}): size = {self.size}, x = {self.x}, y = {self.y}, color = {self.color})"





########################### main game################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()

