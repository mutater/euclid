import sys, pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Throught a given point to draw a straight line parallel to a given straight line.

a = (322, 200)
b = (256, 400)

c = (200, 200)
d = (400, 200)

e = (400, 400)
f = (200, 400)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)
pygame.draw.line(screen, (0, 0, 0), e, f, 2)

pygame.display.flip()

input()