import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((900, 900))

Math = Math()

#variables

a = (450, 240)
b = (350, 420)
c = (a[0] - b[0] + a[0], b[1])
distAB = Math.distance(a[0], a[1], b[0], b[1])
distBC = Math.distance(c[0], c[1], b[0], b[1])
f = (int((b[0]-a[0])*1.5 + b[0]),int((b[1]-a[1])*1.5 + b[1]))
g = (int((c[0]-a[0])*1.5 + c[0]),int((c[1]-a[1])*1.5 + c[1]))
distAF = Math.distance(a[0], a[1], f[0], f[1])
#white screen

screen.fill((255, 255, 255))

# Let ABC be an isosceles triangle having the side AB equal to the side AC;

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), b, c, 2)
pygame.draw.line(screen, (0, 0, 0), c, a, 2)

# and let the straight lines BD, CE be produced further in a straight line with AB, AC

pygame.draw.line(screen, (0, 0, 0), a, ((c[0]-a[0])*2 + c[0],(c[1]-a[1])*2 + c[1]), 2)
pygame.draw.line(screen, (0, 0, 0), a, ((b[0]-a[0])*2 + b[0],(b[1]-a[1])*2 + b[1]), 2)

# Let a point F be taken at random on BD; from AE the greater let AG be cut off equal to AF the less and let the straight lines FC, GB be joined

pygame.draw.circle(screen, (0, 0, 0), a, distAF, 1)
pygame.draw.line(screen, (0, 0, 0), f, c, 2)
pygame.draw.line(screen, (0, 0, 0), g, b, 2)

# program quit

pygame.display.flip()
input()