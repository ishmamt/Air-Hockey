# Here all the Classes will be defined that are used in the game

# imports
import pygame


class Player(object):
    # class def for the player
    def __init__(self, x, y, radius, col=(0, 0, 0)):
        self.points = 0
        self.x = x
        self.y = y
        self.radius = radius
        self.col = col  # default color is black

    def pos(self):
        # return the position of the player
        return (self.x, self.y)

    def draw(self, win):
        # a function to draw the player paddle
        pygame.draw.circle(win, self.col, self.pos(), self.radius)  # win is the window where it will be drawn


class Puck(object):
    # class def for the ingame puck
    def __init__(self, x, y, radius, col=(0, 0, 0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.col = col  # default color is black

    def pos(self):
        # returns position of the puck
        return (self.x, self.y)

    def draw(self, win):
        # a function to draw the player paddle
        pygame.draw.circle(win, self.col, self.pos(), self.radius)  # win is the window where it will be drawn
