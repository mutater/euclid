import pygame, sys
from euclidMath import Math
from pygame.locals import *
pygame.init

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles

a = (300, 340)
b = (234, 436)
c = (342, 436)
d = (369, 436)
e = ((a[0]+c[0])/2, (a[1]+c[1])/2)
f = (e[0]*2-b[0], e[1]-(b[1]-e[1]))

g1 = (c[0] - a[0]) * 2 + a[0]
g2 = (c[1] - a[1]) * 2 + a[1]

g = (g1, g2)

h = ((c[0] - b[0])/2+b[0], (c[1] - a[1])+c[1])


pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), b, c, 2)
pygame.draw.line(screen, (0, 0, 0), f, b, 2)
pygame.draw.line(screen, (0, 0, 0), f, c, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)
pygame.draw.line(screen, (0, 0, 0), c, g, 2)


pygame.draw.line(screen, (0, 0, 0), a, h, 2)
pygame.draw.line(screen, (0, 0, 0), h, c, 2)

pygame.display.flip()
input()