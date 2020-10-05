import pygame, sys
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((600, 600))

Math = Math()

# On a given finite straight line to construct an equilateral triangle.

a = (200, 400)
b = (400, 400)

dist = Math.distance(a[0], a[1], b[0], b[1])

# Fill screen with white
screen.fill((255, 255, 255))

# Let AB be the given finite straight line.
pygame.draw.line(screen, (0, 0, 0), a, b, 2)

# With centre A and sistance AB let the circle BCD be described.
pygame.draw.circle(screen, (0, 0, 0), a, dist, 1)

# With center B and distance BA let the circle ACE be described.
pygame.draw.circle(screen, (0, 0, 0), b, dist, 1)

# From the point C, in which the circles cut one another, to the points A, B let the straight lines CA, CB be joined.
pygame.draw.line(screen, (0, 0, 0), a, (Math.avg(a[0], b[0]), a[1] - Math.pythagac(dist/2, dist)), 2)
pygame.draw.line(screen, (0, 0, 0), b, (Math.avg(a[0], b[0]), a[1] - Math.pythagac(dist/2, dist)), 2)

pygame.display.flip()

input()
