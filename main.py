# this script has the main loop that runs the game

# imports
import pygame
import math
from classdef import Player
from classdef import Puck
from keypress import detect_key

# constants

# screen dimentions
WIDTH = 500
HEIGHT = 700

# initializing the window and clock
win = pygame.display.set_mode((WIDTH, HEIGHT))
clk = pygame.time.Clock()
FPS = 60  # frames per second

# game attributes
PL_SPEED = 5
PUCK_SPEED = 5
PL_RADIUS = 20
PUCK_RADIUS = 10


def redraw():
    # function that redraws all the elements in the window
    win.fill((0, 0, 0))  # fill the screen to remove the last frame
    p1.draw(win)
    p2.draw(win)
    puck.draw(win)
    pygame.display.update()


# instancing the objects for the game
p1 = Player(100, 100, PL_RADIUS, PL_SPEED, WIDTH, 0, HEIGHT / 2, (255, 0, 0))  # fix this harcoded issue and make it accessible by constants
p2 = Player(300, 500, PL_RADIUS, PL_SPEED, WIDTH, HEIGHT / 2, HEIGHT, (0, 255, 0))
puck = Puck(WIDTH // 2, HEIGHT // 2, PUCK_RADIUS, WIDTH, HEIGHT, PUCK_SPEED, (255, 255, 255))

run = True  # for running the main loop
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# anyting between the lines are in the main loop
while run:
    clk.tick(FPS)
    # collecting all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # stop the game if user tries to quit
    keys = pygame.key.get_pressed()
    detect_key(keys, p1, p2)
    p1.hit_detect(puck)
    p2.hit_detect(puck)
    puck.move()
    # print(puck.angle)
    redraw()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pygame.quit()
