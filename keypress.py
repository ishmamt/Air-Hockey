# this script detects all the key presses gives command for movement

# imports
import pygame


def detect_key(keys, p1, p2, puck):
    # this function takes the list of all keys pressed

    # the hit should not be in here as it only can detect moving hits
    if keys[pygame.K_LEFT]:
        p1.move(0)
        p1.hit_detect(puck)
    if keys[pygame.K_RIGHT]:
        p1.move(1)
        p1.hit_detect(puck)
    if keys[pygame.K_UP]:
        p1.move(2)
        p1.hit_detect(puck)
    if keys[pygame.K_DOWN]:
        p1.move(3)
        p1.hit_detect(puck)
    if keys[pygame.K_w]:
        p2.move(2)
        p2.hit_detect(puck)
    if keys[pygame.K_s]:
        p2.move(3)
        p2.hit_detect(puck)
    if keys[pygame.K_a]:
        p2.move(0)
        p2.hit_detect(puck)
    if keys[pygame.K_d]:
        p2.move(1)
        p2.hit_detect(puck)
