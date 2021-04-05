import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Parts of a square add up to a whole

a = (200, 200)
b = (350, 200)
c = (400, 200)
d = (200, 400)
e = (350, 400)
f = (400, 400)
g = (200, 250)
h = (400, 250)

i = (375, 200)
j = (375, 400)

k = (200, 225)
l = (400, 225)

pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), c, f, 2)
pygame.draw.line(screen, (0, 0, 0), f, d, 2)
pygame.draw.line(screen, (0, 0, 0), d, a, 2)
pygame.draw.line(screen, (0, 0, 0), e, b, 2)
pygame.draw.line(screen, (0, 0, 0), g, h, 2)

pygame.draw.line(screen, (0, 0, 0), i, j, 2)
pygame.draw.line(screen, (0, 0, 0), k, l, 2)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()