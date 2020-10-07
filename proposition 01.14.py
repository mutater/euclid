import pygame, sys
from euclidMath import Math
from pygame.locals import *
pygame.init

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straigt line with one another

pygame.draw.line(screen, (0, 0, 0), (-1, 300), (601, 300), 2)
pygame.draw.line(screen, (0, 0, 0), (500, 200), (100, 400), 2)

pygame.display.flip()
input()