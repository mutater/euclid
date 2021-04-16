import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Make square equal to rectilineal figure

a = (100, 200)
b = (100, 300)
c = (200, 300)
d = (200, 200)

e = (250, 225)
f = (250, 275)
g = (350, 225)
h = (350, 275)

i = (400, 200)
j = (400, 300)
k = (500, 300)
l = (500, 200)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)
pygame.draw.line(screen, (0, 0, 0), d, a, 2)

pygame.draw.line(screen, (0, 0, 0), e, g, 2)
pygame.draw.line(screen, (0, 0, 0), f, h, 2)

pygame.draw.line(screen, (0, 0, 0), i, j, 2)
pygame.draw.line(screen, (0, 0, 0), j, k, 2)
pygame.draw.line(screen, (0, 0, 0), k, l, 2)
pygame.draw.line(screen, (0, 0, 0), i, l, 2)




pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

