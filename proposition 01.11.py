import pygame, sys
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((600, 600))

Math = Math()

# To draw a straight line at right angles to a given sdtraight line from a given point on it.

a = (0, 400)
b = (600, 400)
c = (300, 400)
d = (100, 400)
e = (500, 400)

dist = Math.distance(d[0], d[1], e[0], e[1])

f = (Math.avg(d[0], e[0]), d[1] - Math.pythagac(dist/2, dist))

# Fill the screen with white.

screen.fill((255, 255, 255))

# Let AB be the given straight line, and C the given point on it.

pygame.draw.line(screen, (0, 0, 0), a, b, 2)

# Let a point D be taken at random on AC; let Ce be made equal to CD; on DE let the equilater triangle FDE be constructed, and let FC be joined.

pygame.draw.circle(screen, (0, 0, 0), c, Math.distance(d[0], 0, c[0], 0), 1)

pygame.draw.line(screen, (0, 0, 0), d, f, 2)
pygame.draw.line(screen, (0, 0, 0), e, f, 2)

pygame.draw.line(screen, (0, 0, 0), c, f, 2)

pygame.display.flip()

input()
