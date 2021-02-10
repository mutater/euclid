import sys, pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#If a striaght line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another

a = (100, 250)
b = (500, 250)
c = (100, 350)
d = (500, 350)

e = (500, 50)
f = (50, 500)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)
pygame.draw.line(screen, (0, 0, 0), f, e, 2)

pygame.display.flip()

input()