import sys, pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# The straight lines jaining equal and parallel straight lines [at the extremities which are] in the same directions [repsectively] are themselves also equal and parallel.

a = (200, 200)
b = (400, 200)
c = (190, 400)
d = (390, 400)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), d, c, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)

pygame.display.flip()

input()