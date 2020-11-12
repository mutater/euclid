import sys, pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# If on one of the sides of a triangle,from its extremities, there be constructed two straight lines
# meeting within the triangle, the straight lines so construected will be less than the remaining 
# two sides of the triangle, but will contain a greater angle.

a = (200, 200)
b = (300, 150)
c = (300, 300)
d = (275, 200)
e = (250, 250)


pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), d, b, 2)
pygame.draw.line(screen, (0, 0, 0), e, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)


pygame.display.flip()
input()
