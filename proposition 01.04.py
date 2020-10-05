import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((900, 900))

Math = Math()

# variables
a = (30, 342)
b = (303, 546)
c = (335, 542)

d = (430, 342)
e = (703, 546)
f = (735, 542)

#white screen

screen.fill((255, 255, 255))

# Let ABC, DEF be two triangles having the two sides AB, AC equal to the two sides DE, DF respectively

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), b, c, 2)
pygame.draw.line(screen, (0, 0, 0), c, a, 2)
pygame.draw.line(screen, (0, 0, 0), d, e, 2)
pygame.draw.line(screen, (0, 0, 0), e, f, 2)
pygame.draw.line(screen, (0, 0, 0), f, d, 2)


pygame.display.flip()
input()