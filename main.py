# this script has the main loop that runs the game

# imports
import pygame
import math

# constants

# screen dimentions
WIDTH = 700
HEIGHT = 900

# initializing the window and clock
win = pygame.display.set_mode((WIDTH, HEIGHT))
clk = pygame.time.Clock()
FPS = 60  # frames per second


def redraw():
    # function that redraws all the elements in the window
    pass


run = True  # for running the main loop
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# anyting between the lines are in the main loop
while run:
    clk.tick(FPS)
    # collecting all the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # stop the game if user tries to quit
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pygame.quit()
