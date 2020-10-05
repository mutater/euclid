import pygame, sys
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((600, 600))

Math = Math()

#To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.

#make it so the screen isn't a void

screen.fill((255, 255, 255))

#"Infinate line"

pygame.draw.line(screen, (0, 0, 0), (-1, 400), (601, 400), 2)

#key points

d = (453, 563)
c = (300, 350)
distCD = Math.distance(d[0], d[1], c[0], c[1])

h = (c[0], 400)
distCH = h[1] - c[1]
distCE = Math.pythagac(distCH, distCD)
e = (c[0] + distCE, 400)
g = (c[0] - distCE, 400)

#circle, and perpendicular line

pygame.draw.circle(screen, (0, 0, 0), c, distCD, 2)
pygame.draw.line(screen, (0, 0, 0), c, (c[0], 400), 2)

#lines going from C to the point where the circle touches the the line

pygame.draw.line(screen, (0, 0, 0), c, e, 2)
pygame.draw.line(screen, (0, 0, 0), c, g, 2)

pygame.display.flip()

input()