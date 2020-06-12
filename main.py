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


def redraw():
    # function that redraws all the elements in the window
    win.fill((0, 0, 0))  # fill the screen to remove the last frame
    p1.draw(win)
    p2.draw(win)
    puck.draw(win)
    pygame.display.update()


# instancing the objects for the game
p1 = Player(100, 100, 20, 3, WIDTH, 0, HEIGHT / 2, (255, 0, 0))  # fix this harcoded issue
p2 = Player(300, 500, 20, 3, WIDTH, HEIGHT / 2, HEIGHT, (0, 255, 0))
puck = Puck(400, 200, 15, (255, 255, 255))

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
    detect_key(keys, p1, p2, puck)
    redraw()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pygame.quit()
