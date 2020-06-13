# Here all the Classes will be defined that are used in the game

# imports
import pygame


class Player(object):
    # class def for the player
    def __init__(self, x, y, radius, vel, WIDTH, H_START, H_END, col=(0, 0, 0)):
        self.points = 0
        self.x = x
        self.y = y
        self.radius = radius
        self.col = col  # default color is black
        self.vel = vel
        self.WIDTH = WIDTH
        self.H_START = H_START
        self.H_END = H_END
        self.moving = False
        self.mov_up = False
        self.mov_down = False
        self.mov_left = False
        self.mov_right = False

    def pos(self):
        # return the position of the player
        return (self.x, self.y)

    def draw(self, win):
        # a function to draw the player paddle
        pygame.draw.circle(win, self.col, self.pos(), self.radius)  # win is the window where it will be drawn
        # the hit box
        pygame.draw.rect(win, (255, 255, 255), (self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius), 1)

    def setmove(self, dir):
        # resets any movement
        self.mov_up = False
        self.mov_down = False
        self.mov_left = False
        self.mov_right = False
        if dir == 0:
            self.mov_left = True
            self.moving = True
        elif dir == 1:
            self.mov_right = True
            self.moving = True
        elif dir == 2:
            self.mov_down = True
            self.moving = True
        elif dir == 3:
            self.mov_up = True
            self.moving = True
        else:
            self.moving = False
            self.mov_down = False
            self.mov_up = False
            self.mov_left = False
            self.mov_right = False

    def move(self, dir):
        if dir == 0:
            if self.x - self.vel >= self.radius:
                self.x -= self.vel
        elif dir == 1:
            if self.x + self.vel <= self.WIDTH - self.radius:
                self.x += self.vel
        elif dir == 2:
            if self.y - self.vel >= self.H_START + self.radius:
                self.y -= self.vel
        elif dir == 3:
            if self.y + self.vel <= self.H_END - self.radius:
                self.y += self.vel

    def hit_detect(self, puck):
        # detects when the player hits the puck
        if ((self.y + self.radius) >= (puck.y - puck.radius)) and ((self.y + self.radius) <= (puck.y + puck.radius)):
            if (((puck.x - puck.radius) >= (self.x - self.radius)) and ((puck.x - puck.radius) <= (self.x + self.radius))) or (((puck.x + puck.radius) >= (self.x - self.radius)) and ((puck.x + puck.radius) <= (self.x + self.radius))):
                print('HIT', self.x, self.y)
        elif ((self.y - self.radius) <= (puck.y + puck.radius)) and ((self.y - self.radius) >= (puck.y - puck.radius)):
            if (((puck.x - puck.radius) >= (self.x - self.radius)) and ((puck.x - puck.radius) <= (self.x + self.radius))) or (((puck.x + puck.radius) >= (self.x - self.radius)) and ((puck.x + puck.radius) <= (self.x + self.radius))):
                print('HIT', self.x, self.y)

    def calcAngle(self, puck):
        pass


class Puck(object):
    # class def for the ingame puck
    def __init__(self, x, y, radius, col=(0, 0, 0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.col = col  # default color is black
        self.angle = 0  # the angle that the puck will move

    def pos(self):
        # returns position of the puck
        return (self.x, self.y)

    def draw(self, win):
        # a function to draw the puck
        pygame.draw.circle(win, self.col, self.pos(), self.radius)  # win is the window where it will be drawn
        # the hit box
        pygame.draw.rect(win, (255, 0, 0), (self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius), 1)

    def move(self):
        pass
