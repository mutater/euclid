import sys, pygamne
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# In parallelogrammic areas the opposite dies and angles are equal to one another and the diameter bisects the areas

a = (200, 200)
b = (400, 200)
c = (190, 400)
d = (390, 400)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), d, c, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 1)

pygame.display.flip()

input()