# this script detects all the key presses gives command for movement

# imports
import pygame


def detect_key(keys, p1, p2, puck):
    # this function takes the list of all keys pressed
    if keys[pygame.K_LEFT]:
        p1.move(0)
    elif keys[pygame.K_RIGHT]:
        p1.move(1)
    elif keys[pygame.K_UP]:
        p1.move(2)
    elif keys[pygame.K_DOWN]:
        p1.move(3)
    elif keys[pygame.K_w]:
        p2.move(2)
    elif keys[pygame.K_s]:
        p2.move(3)
    elif keys[pygame.K_a]:
        p2.move(0)
    elif keys[pygame.K_d]:
        p2.move(1)
