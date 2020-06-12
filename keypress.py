# this script detects all the key presses gives command for movement

# imports
import pygame


def detect_key(keys):
    # this function takes the list of all keys pressed
    if keys[pygame.K_LEFT]:
        print('left')
    elif keys[pygame.K_RIGHT]:
        print('right')
    elif keys[pygame.K_UP]:
        print('up')
    elif keys[pygame.K_DOWN]:
        print('down')
    elif keys[pygame.K_w]:
        print('w')
    elif keys[pygame.K_s]:
        print('s')
    elif keys[pygame.K_a]:
        print('a')
    elif keys[pygame.K_d]:
        print('d')
