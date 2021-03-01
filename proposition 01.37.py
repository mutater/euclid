import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Triangles with the same base and the top of said triangles touching a line parallel to the bases of the triangle, the triangles will be equal.

a = (200, 400)
b = (400, 400)
c = (250, 200)
d = (300, 200)

e = (100, 200)
f = (500, 200)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)

pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)

pygame.draw.line(screen, (0, 0, 0), d, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)

pygame.draw.line(screen, (0, 0, 0), e, f, 1)

pygame.display.flip()

input()