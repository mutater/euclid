import pygame, sys
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

Math = Math()

#On a given straight line and at a point on it to construct a rectilineal ange equal to a given rectilineal angle

a = (100, 400)
b = (500, 400)
c = (200, 250)
d = (349, 163)
e = (369, 250)

distCE = Math.vardist(c, e)

distDE = int(Math.vardist(e, d)/3.43)

f = (a[0] + distCE, a[1])
g = (a[0] + distCE, a[1] - distDE)


pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), d, c, 2)
pygame.draw.line(screen, (0, 0, 0), d, e, 2)
pygame.draw.line(screen, (0, 0, 0), e, c, 2)
pygame.draw.line(screen, (0, 0, 0), a, g, 2)
pygame.draw.line(screen, (0, 0, 0), f, g, 2)

pygame.draw.circle(screen, (0, 0, 0), f, 3, 3)

pygame.display.flip()

input()