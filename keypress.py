# this script detects all the key presses gives command for movement

# imports
import pygame


def detect_key(keys, p1, p2):
    # this function takes the list of all keys pressed
    if keys[pygame.K_LEFT]:
        p1.move(0)
    if keys[pygame.K_RIGHT]:
        p1.move(1)
    if keys[pygame.K_UP]:
        p1.move(2)
    if keys[pygame.K_DOWN]:
        p1.move(3)
    if keys[pygame.K_w]:
        p2.move(2)
    if keys[pygame.K_s]:
        p2.move(3)
    if keys[pygame.K_a]:
        p2.move(0)
    if keys[pygame.K_d]:
        p2.move(1)
