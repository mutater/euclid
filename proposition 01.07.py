import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((600, 600))

Math = Math()

# Given two straight lines constructed on a straight line and meeting in a point, there cannot be constructed on the same straight line, and on the same side of it,
# two other straight lines meeting in another point and equal to the former two repsectively, namely each to that which has the same extremity with it.

a = (100, 500)
b = (500, 500)
c = (300, 200)
d = (400, 250)

# screen fill

screen.fill((255, 255, 255))

# For, if possible, given two straihgt lines AC, CB constructed on the straight line AB and meeting at the point C, let two other straight lines AD, DB be constructed
# on the same straight line AB, on the same side of it, meeting in another point D and equal to the former two respectively

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)
pygame.draw.line(screen, (0, 0, 0), b, c, 2)
pygame.draw.line(screen, (0, 0, 0), b, d, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)

pygame.display.flip()
input()