# this script has the main loop that runs the game

# imports
import pygame
from classdef import Player
from classdef import Puck
from keypress import detect_key
import gui
import logging


# constants

# screen dimentions
WIDTH = 500
HEIGHT = 700

# initializing the window and clock
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Air Hockey')
clk = pygame.time.Clock()
FPS = 60  # frames per second

# game attributes
PL_SPEED = 6  # player movement speed
PUCK_SPEED = 5  # maximum velocity of the puck
PL_RADIUS = 20
PUCK_RADIUS = 10
GOAL_WIDHT = 150
GOAL_HEIGHT = 10
background = pygame.image.load('gameBG.jpg')
score_font = pygame.font.SysFont('Microsoft YaHei Light', 30)

# music
pygame.mixer.init()
bgMusic = pygame.mixer.music.load('bgMusic.mp3')
pygame.mixer.music.play(-1)

# making the goals as a rect object
p1_goal = pygame.Rect(WIDTH // 2 - GOAL_WIDHT // 2, 0, GOAL_WIDHT, GOAL_HEIGHT)
p2_goal = pygame.Rect(WIDTH // 2 - GOAL_WIDHT // 2, HEIGHT - GOAL_HEIGHT, GOAL_WIDHT, GOAL_HEIGHT)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOAL_COL = (102, 102, 255)
P1_COL = (232, 38, 38)
P2_COL = (70, 180, 88)
SCORE_COL = (191, 191, 191)

# setting up a logger
logging.basicConfig(filename='history.log', format='%(asctime)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger()  # getting an object called logger


def drawBoard():
    # This function draws the game board
    pygame.draw.line(win, WHITE, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2))
    pygame.draw.circle(win, WHITE, (WIDTH // 2, HEIGHT // 2), 100, 1)

    pygame.draw.rect(win, GOAL_COL, p1_goal, 3)
    pygame.draw.rect(win, GOAL_COL, p2_goal, 3)

    p1Score = score_font.render(f'{p1.name} : {p1.points}', 1, SCORE_COL)
    p2Score = score_font.render(f'{p2.name} : {p2.points}', 1, SCORE_COL)
    win.blit(p1Score, (10, 5))
    win.blit(p2Score, (WIDTH - 160, 5))


def redraw():
    # function that redraws all the elements in the window
    # win.fill(BLACK)  # fill the screen to remove the last frame
    win.blit(background, (0, 0))
    p1.draw(win)
    p2.draw(win)
    puck.draw(win)
    drawBoard()
    pygame.display.update()


# instancing the objects for the game
p1 = Player(100, 100, PL_RADIUS, PL_SPEED, WIDTH, 0, HEIGHT / 2, P1_COL)  # fix this harcoded issue and make it accessible by constants
p2 = Player(300, 500, PL_RADIUS, PL_SPEED, WIDTH, HEIGHT / 2, HEIGHT, P2_COL)
puck = Puck(WIDTH // 2, HEIGHT // 2, PUCK_RADIUS, WIDTH, HEIGHT, PUCK_SPEED, WHITE)


gui.mainLoop(p1, p2)  # handles the GUI
pygame.time.delay(400)  # slight delay after the title screen


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
    if puck.inGoal(p1, p2, p1_goal, p2_goal, win, logger):
        run = False  # game over
    redraw()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pygame.quit()
