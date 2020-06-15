# Here all the Classes will be defined that are used in the game

# imports
import pygame
import math


class Player(object):
    # class def for the player
    def __init__(self, x, y, radius, vel, WIDTH, H_START, H_END, col=(255, 255, 255)):
        self.points = 0
        self.x = x
        self.y = y
        self.radius = radius
        self.col = col  # default color is white
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
        # this finds the angle between the puck and the player if a hit happens
        if self.mov_up:
            moveAngle = math.pi / 2  # this is the angle of the players dir with respect to the x axis
        elif self.mov_down:
            moveAngle = (3 * math.pi) / 4
        elif self.mov_right:
            moveAngle = 0
        elif self.mov_left:
            moveAngle = math.pi
        else:
            moveAngle = None  # if the player is stationary

        # now we calculate the angle at which the puck hits the paddle
        try:
            hitAngle = math.atan((puck.y - self.y) / (puck.x - self.x))
        except:
            hitAngle = math.pi / 2
        # correcting for the angle to stay in [-2pi ~ 2pi]
        if puck.x >= self.x and puck.y <= self.y:
            hitAngle = abs(hitAngle)
        elif puck.x < self.x and puck.y <= self.y:
            hitAngle = math.pi - hitAngle
        elif puck.x < self.x and puck.y > self.y:
            hitAngle = math.pi + abs(hitAngle)
        else:
            hitAngle = 2 * math.pi - hitAngle

        # finally finding the difference between the paddle's direction and the hitAngle
        puck.angle = 10  # NEEDS TO BE FIXED


class Puck(object):
    # class def for the ingame puck
    def __init__(self, x, y, radius, WIDTH, HEIGHT, maxVel=5, col=(0, 0, 0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.maxVel = maxVel
        self.col = col  # default color is black
        self.angle = math.pi / 4  # the angle that the puck moves
        # these x, y pair will keep the position of the puck in the last frame for angle calculation
        self.lastx = x
        self.lasty = y

    def pos(self):
        # returns position of the puck
        return (self.x, self.y)

    def draw(self, win):
        # a function to draw the puck
        pygame.draw.circle(win, self.col, self.pos(), self.radius)  # win is the window where it will be drawn
        # the hit box
        pygame.draw.rect(win, (255, 0, 0), (self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius), 1)

    def staticHitAngle(self):
        # this func will calculate the angle of which the puck would move in the case of a static obj collision eg: wall
        pass

    def move(self):
        self.lastx = self.x  # keeping track of the last frames position before moving
        self.lasty = self.y
        # self.x += round(math.cos(self.angle) * self.maxVel)
        # self.y -= round(math.sin(self.angle) * self.maxVel)
        newx = round(math.cos(self.angle) * self.maxVel)
        newy = round(math.sin(self.angle) * self.maxVel)
        if self.x + newx >= self.radius and self.x + newx <= self.WIDTH - self.radius:
            if self.y - newy >= self.radius and self.y - newy <= self.HEIGHT - self.radius:
                self.x += newx
                self.y -= newy
