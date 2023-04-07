from Constants import *
#basic sprite system from our old program
#kind of obsolete after finding pygame methods
class Sprite:
    def __init__(self):
        pass


    def getPosition(self):
        # calculate the position of the sprite
        return self.x, self.y

    def goUp(self, move=0.5):
        self.y -= move
    def goDown(self, move=0.5):
        self.y += move
    def goLeft(self, move=0.5):
        self.x -= move
    def goRight(self, move=0.5):
        self.x += move

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        # checks for x being larger than the max or smaller than 0
        if x > MAX_X - 50:
            self._x = MAX_X - 50
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