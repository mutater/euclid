import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# On a given straight line to describe a square

a = (200, 200)
b = (400, 200)
c = (200, 400)
d = (400, 400)

e = (200, 50)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), d, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)

pygame.draw.line(screen, (0, 0, 0), c, e, 2)

pygame.display.flip()

input()