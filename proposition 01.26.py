import sys, pygame
from pygame.locals import *
pygame.init()

pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# If two triangles have the two angles qual to two angles respectively, and one side equal to one side, namely, 
# either the side adjoining the equal angles or that subtending one of the equal angles, they will also have the remaining sides 
# equal to the remaining sides and the remaining angle to the remaining angle

a = (100, 200)
b = (200, 300)
c = (300, 100)

d = (400, 200)
e = (500, 300)
f = (600, 100)


pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), d, e, 2)
pygame.draw.line(screen, (0, 0, 0), d, f, 2)
pygame.draw.line(screen, (0, 0, 0), f, e, 2)

pygame.display.flip()
input()
