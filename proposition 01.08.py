import sys, pygame, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((1200, 600))

Math = Math()

# If a triangle has all sides equal to another triangles sides, then the corrisponding angles will be equal.

a = (200, 200)
b = (350, 300)
c = (130, 453)

d = (a[0]+600, a[1])
e = (b[0]+600, b[1])
f = (c[0]+600, c[1])

g = (900, 153)
h = e
i = f

# fill screen

screen.fill((255, 255, 255))

# Triangle ABC

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), b, c, 2)
pygame.draw.line(screen, (0, 0, 0), c, a, 2)

# Triangle DEF

pygame.draw.line(screen, (0, 0, 0), d, e, 2)
pygame.draw.line(screen, (0, 0, 0), e, f, 2)
pygame.draw.line(screen, (0, 0, 0), f, d, 2)

# Another one

pygame.draw.line(screen, (0, 0, 0), g, h, 2)
pygame.draw.line(screen, (0, 0, 0), h, i, 2)
pygame.draw.line(screen, (0, 0, 0), i, g, 2)

# We must destroy germany

pygame.display.flip()
input()