import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#A straight line falling on parallel straight lines makes the alternate angles ueqal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles

a = (100, 250)
b = (500, 250)
c = (100, 350)
d = (500, 350)

e = (500, 50)
f = (50, 500)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)
pygame.draw.line(screen, (0, 0, 0), e, f, 2)

pygame.display.flip()
input()