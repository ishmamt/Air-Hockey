# Here all the Classes will be defined that are used in the game

# imports
import pygame


class Player(object):
    # class def for the player
    def __init__(self, x, y, radius, vel, col=(0, 0, 0)):
        self.points = 0
        self.x = x
        self.y = y
        self.radius = radius
        self.col = col  # default color is black
        self.vel = vel

    def pos(self):
        # return the position of the player
        return (self.x, self.y)

    def draw(self, win):
        # a function to draw the player paddle
        pygame.draw.circle(win, self.col, self.pos(), self.radius)  # win is the window where it will be drawn

    def move(self, dir, WIDHT, HEIGHT):
        if dir == 0:
            if self.x - self.vel >= self.radius:
                self.x -= self.vel
        elif dir == 1:
            if self.x + self.vel <= WIDHT - self.radius:
                self.x += self.vel
        elif dir == 2:
            if self.y - self.vel >= self.radius:
                self.y -= self.vel
        elif dir == 3:
            if self.y + self.vel <= HEIGHT - self.radius:
                self.y += self.vel


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

    def move(self):
        pass
