import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Same thing as 02 but it's a rectangle

a = (100, 200)
b = (350, 200)
c = (500, 200)
d = (100, 400)
e = (350, 400)
f = (500, 400)

pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), c, f, 2)
pygame.draw.line(screen, (0, 0, 0), f, d, 2)
pygame.draw.line(screen, (0, 0, 0), d, a, 2)
pygame.draw.line(screen, (0, 0, 0), e, b, 2)

pygame.display.flip()

input()
