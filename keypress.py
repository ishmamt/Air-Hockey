# this script detects all the key presses gives command for movement

# imports
import pygame


def detect_key(keys, p1, p2):
    # this function takes the list of all keys pressed

    # the hit should not be in here as it only can detect moving hits
    if keys[pygame.K_LEFT]:
        p2.move(0)
    if keys[pygame.K_RIGHT]:
        p2.move(1)
    if keys[pygame.K_UP]:
        p2.move(2)
    if keys[pygame.K_DOWN]:
        p2.move(3)
    if keys[pygame.K_w]:
        p1.move(2)
    if keys[pygame.K_s]:
        p1.move(3)
    if keys[pygame.K_a]:
        p1.move(0)
    if keys[pygame.K_d]:
        p1.move(1)
    if not keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        p2.moving = False
    if not keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
        p1.moving = False
