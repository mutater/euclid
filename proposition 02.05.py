import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# The large rectangle + the square using the mini rectangle's short side equal the square of half the length of the line

a = (100, 200)
b = (250, 200)
c = (300, 200)
d = (100, 400)
e = (250, 400)
f = (300, 400)
g = (100, 250)
h = (300, 250)

i = (500, 250)
j = (500, 400)

pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), c, f, 2)
pygame.draw.line(screen, (0, 0, 0), f, d, 2)
pygame.draw.line(screen, (0, 0, 0), d, a, 2)
pygame.draw.line(screen, (0, 0, 0), e, b, 2)
pygame.draw.line(screen, (0, 0, 0), g, h, 2)

pygame.draw.line(screen, (0, 0, 0), i, g, 2)
pygame.draw.line(screen, (0, 0, 0), j, f, 2)
pygame.draw.line(screen, (0, 0, 0), i, j, 2)

pygame.display.flip()

input()
