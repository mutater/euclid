import sys, pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#If a straight line falling on two straight lines make the exterior angle equal to the interior and opposite angle on the same side, or the interior angles on the same side equal to tow right angles, the straight lines will be parallel to one another

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