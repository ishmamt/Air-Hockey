# this script detects all the key presses gives command for movement

# imports
import pygame


def detect_key(keys, p1, p2):
    # this function takes the list of all keys pressed

    # the hit should not be in here as it only can detect moving hits
    if keys[pygame.K_LEFT]:
        p1.setmove(0)
        p1.move(0)
    elif keys[pygame.K_RIGHT]:
        p1.setmove(1)
        p1.move(1)
    elif keys[pygame.K_UP]:
        p1.setmove(2)
        p1.move(2)
    elif keys[pygame.K_DOWN]:
        p1.setmove(3)
        p1.move(3)
    else:
        p1.moving = False
        p1.setmove(10)  # any number other than (0~3)
    if keys[pygame.K_w]:
        p2.setmove(2)
        p2.move(2)
    elif keys[pygame.K_s]:
        p2.setmove(3)
        p2.move(3)
    elif keys[pygame.K_a]:
        p2.setmove(0)
        p2.move(0)
    elif keys[pygame.K_d]:
        p2.setmove(1)
        p2.move(1)
    else:
        p2.moving = False
        p2.setmove(10)  # any number other than (0~3)
