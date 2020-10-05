import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((800, 800))

Math = Math()

# To place at a given point a straight line euqal to a given straight line.

a = (300, 420)
b = (420, 420)
c = (269, 242)
distAB = Math.distance(a[0], a[1], b[0], b[1])
distBC = Math.distance(c[0], c[1], b[0], b[1])
d = (Math.avg(a[0], b[0]), a[1] - Math.pythagac(distAB/2, distAB))
distDB = Math.distance(d[0], d[1], b[0], b[1])

# Fill screen with white.

screen.fill((255, 255, 255))

# Let A be the given point, and BC the given straight line.

pygame.draw.circle(screen, (0, 0, 0), a, 2)
pygame.draw.line(screen, (0, 0, 0), b, c, 2)

# Thus it is required to place at the point A a straight line equal to the given straight line BC.
# From the point A to the point B let the straight line AB be joined; and on it let the equilateral triangle DAB be constructed.

pygame.draw.line(screen, (0, 0, 0), a, b, 1)

pygame.draw.line(screen, (0, 0, 0), a, d, 1)
pygame.draw.line(screen, (0, 0, 0), b, d, 1)

# Let the straight lines AE, BF be produced in a straight line with DA, DB

pygame.draw.line(screen, (0, 0, 0), d, ((a[0]-d[0])*2 + a[0],(a[1]-d[1])*2 + a[1]), 2)
pygame.draw.line(screen, (0, 0, 0), d, ((b[0]-d[0])*2 + b[0],(b[1]-d[1])*2 + b[1]), 2)

# With centre B and distance BC let the circle CGH be described; and with centre D and distance DG let the circle GKL be described.

pygame.draw.circle(screen, (0, 0, 0), b, distBC, 2)
pygame.draw.circle(screen, (0, 0, 0), d, distBC + distDB, 2)

pygame.display.flip()
input()


