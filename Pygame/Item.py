#####################################################################
# author:Grant Cooper
# date:3/9/2023
# description: Class takes in input and plots a person to a point. Person can be
# within 0 to 800 or 0 to 600 on the graph for x and y respectively
# the person then can have its distance calculated from aother person in the class.
#####################################################################
from math import sqrt

# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 1000
MAX_Y = 800

# A class representing a person. A person can be initialized with a
# name, as well as x and y coordinates. However, there are default
# values for all those (i.e. player 1, 0 and 0 respectively). A person
# also has a size which is set to 1 by default. A person can go left,
# go right, go up and go down. A person also has a string function
# that prints out their name location, and size. A person also has a
# function that calculates the euclidean distance from another person
# object.


class Item:
    def __init__(self, name="player1", x=0, y=0):
        self._name: str = name
        self.x: int = x
        self.y: int = y

    size: float = 1

    #size accessor and mutator
    @property
    def getSize(self):
        return self.size
    @getSize.setter
    def setSize(self, size):
        #checks to see if the size is going out of bounds
        tempsize = self.size
        self._size = size
        if self._size < 0:
            self._size = tempsize


    #name accessor and mutator
    @property
    def name(self):
        return self._name
    @name.setter
    #checks name to be greater than a string of 2 characters
    def name(self, name):
        if len(name) >= 2:
            self._name = name
        else:
            self.name = "player1"
    #x accessor and mutator
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        #checks for x being larger than the max or smaller than 0
        if x > MAX_X:
            self._x = MAX_X
        elif x <= 0:
            self._x = 0
        else:
            self._x = x
    #y accessor and mutator
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, y):
        #checks for y being larger than the max or smaller than 0
        if y > MAX_Y:
            self._y = MAX_Y
        elif y <= 0:
            self._y = 0
        else:
            self._y = y

    def goUp(self, move=1):
        self.y -= move
    def goDown(self, move=1):
        self.y += move
    def goLeft(self, move=1):
        self.x -= move
    def goRight(self, move=1):
        self.x += move

    def getDistance(self, other):
        #euclidean distance algorithm
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        return f"Person({self.name}): size = {self.size}, x = {self.x}, y = {self.y})"
