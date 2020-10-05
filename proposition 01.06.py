import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((1000, 1000))

Math = Math()

# Equal angles have equal sides to those who subtend it

a = (500, 300)
b = (372, 575)
c = (a[0]-b[0]+a[0], b[1])
d = ((b[0] + a[0])/2, (a[1] + b[1])/2)

# screen fill

screen.fill((255, 255, 255))

# Let ABC be a traingle having the angle ABC equal to the angle ACB

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), b, c, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)

# Let point D be taken less than and equal to ab, ac respectivly and let cd be joined


pygame.draw.line(screen, (0, 0, 0), c, d, 2)


pygame.display.flip()
input()