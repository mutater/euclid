import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Same as the last proposition butsing 2 rectangles and a big and small square (You'll see)

a = (300, 200)
b = (450, 200)
c = (500, 200)
d = (300, 400)
e = (450, 400)
f = (500, 400)
g = (300, 250)
h = (500, 250)

i = (100, 200)
j = (100, 250)

pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), c, f, 2)
pygame.draw.line(screen, (0, 0, 0), f, d, 2)
pygame.draw.line(screen, (0, 0, 0), d, a, 2)
pygame.draw.line(screen, (0, 0, 0), e, b, 2)
pygame.draw.line(screen, (0, 0, 0), g, h, 2)

pygame.draw.line(screen, (0, 0, 0), i, a, 2)
pygame.draw.line(screen, (0, 0, 0), j, g, 2)
pygame.draw.line(screen, (0, 0, 0), i, j, 2)

pygame.display.flip()

input()