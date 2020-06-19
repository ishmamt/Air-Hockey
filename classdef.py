# Here all the Classes will be defined that are used in the game
# all the physics are handled in this script

# imports
import pygame


# constants
WIDHT = 500
HEIGHT = 700
MAXPOINTS = 2


class Player(object):
    # class def for the player
    def __init__(self, x, y, radius, vel, WIDTH, H_START, H_END, col=(255, 255, 255), name=''):
        self.points = 0
        self.x = x
        self.y = y
        self.radius = radius
        self.col = col  # default color is white
        self.vel = vel  # velocity at which the player can move
        self.WIDTH = WIDTH
        self.H_START = H_START
        self.H_END = H_END
        self.name = name
        self.hitbox = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
        self.moving = False

    def pos(self):
        # return the position of the player
        return (self.x, self.y)

    def draw(self, win):
        # a function to draw the player paddle
        pygame.draw.circle(win, self.col, self.pos(), self.radius)  # win is the window where it will be drawn
        # the hit box drawn for debugging purposes
        self.hitbox.x = self.x - self.radius
        self.hitbox.y = self.y - self.radius
        # pygame.draw.rect(win, (255, 255, 255), self.hitbox, 1)

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
        self.moving = True

    def hit_detect(self, puck):
        # detects if the puck has hit the player
        if self.hitbox.colliderect(puck.hitbox):
            puck.hit(self)

    def goal(self):
        # this function handles the actions if a goal occurs
        if self.points < MAXPOINTS:
            self.points += 1
            return False
        # game is over
        print('GAME OVER')
        print(self.name, 'has won !!')
        return True


class Puck(object):
    # class def for the ingame puck
    def __init__(self, x, y, radius, WIDTH, HEIGHT, maxVel=5, col=(255, 255, 255)):
        self.x = x
        self.y = y
        self.radius = radius
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.maxVel = maxVel
        self.col = col  # default color is white
        self.dx = -maxVel
        self.dy = maxVel
        self.hitbox = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
        self.minVel = 1

    def pos(self):
        # returns position of the puck
        return (self.x, self.y)

    def draw(self, win):
        # a function to draw the puck
        pygame.draw.circle(win, self.col, self.pos(), self.radius)  # win is the window where it will be drawn
        # the hit box drawn for debugging purposes
        self.hitbox.x = self.x - self.radius
        self.hitbox.y = self.y - self.radius
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)

    def hit(self, player):
        # this function is triggered when the puck hits the paddle
        hitMargin = 10  # this is a tolerance margin, any pixel difference under this value is acceptable

        if player.moving:
            # this will increase the speed of the puck when it hits a moving paddle
            # this has no actual purpose right now. I thought about slowing down the puck
            # but that funtionality has not been added yet
            if self.dx > 0:
                self.dx = self.maxVel
            else:
                self.dx = -self.maxVel
            if self.dy > 0:
                self.dy = self.maxVel
            else:
                self.dy = -self.maxVel

        if abs(self.hitbox.bottom - player.hitbox.top) < hitMargin and self.dy < 0:
            self.dy *= -1
        elif abs(self.hitbox.top - player.hitbox.bottom) < hitMargin and self.dy > 0:
            self.dy *= -1
        elif abs(self.hitbox.left - player.hitbox.right) < hitMargin and self.dx < 0:
            self.dx *= -1
        elif abs(self.hitbox.right - player.hitbox.left) < hitMargin and self.dx > 0:
            self.dx *= -1

    def move(self):
        if self.dx > self.maxVel or self.dx < -self.maxVel:
            if self.dx > 0:
                self.dx = self.maxVel
            else:
                self.dx = -self.maxVel
        if self.dy > self.maxVel or self.dy < -self.maxVel:
            if self.dy > 0:
                self.dy = self.maxVel
            else:
                self.dy = -self.maxVel

        # to keep the puck in bounds
        if self.x + self.dx >= self.WIDTH - self.radius or self.x + self.dx <= self.radius:
            self.dx *= -1
        if self.y - self.dy >= self.HEIGHT - self.radius or self.y - self.dy <= self.radius:
            self.dy *= -1

        self.x += round(self.dx)
        self.y -= round(self.dy)

    def inGoal(self, p1, p2, p1_goal, p2_goal):
        if self.hitbox.colliderect(p1_goal):
            print('point for p2')
            self.resetPos()
            return p2.goal()
        if self.hitbox.colliderect(p2_goal):
            print('point for p1')
            self.resetPos()
            return p1.goal()
        return False

    def resetPos(self):
        self.x = WIDHT // 2
        self.y = HEIGHT // 2
