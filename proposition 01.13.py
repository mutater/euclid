import pygame, sys
from euclidMath import Math
from pygame.locals import *
pygame.init

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles

pygame.draw.line(screen, (0, 0, 0), (-1, 400), (601, 400), 2)
pygame.draw.line(screen, (0, 0, 0), (300, 200), (300, 400), 2)
pygame.draw.line(screen, (0, 0, 0), (320, 220), (300, 400), 2)

pygame.display.flip()

input()
