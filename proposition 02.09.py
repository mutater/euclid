import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# bigg square and smool-ish square add up to 2x half line square plus very smool square

a1 = (100, 400)
a2 = (300, 400)
a3 = (300, 200)
a4 = (100, 200)

b1 = (350, 400)
b2 = (350, 350)
b3 = (300, 350)

c1 = (100, 150)
c2 = (350, 150)

d1 = (500, 400)
d2 = (500, 250)
d3 = (350, 250)

pygame.draw.line(screen, (0, 0, 0), a1, a2, 2)
pygame.draw.line(screen, (0, 0, 0), a3, a2, 2)
pygame.draw.line(screen, (0, 0, 0), a3, a4, 2)
pygame.draw.line(screen, (0, 0, 0), a1, a4, 2)

pygame.draw.line(screen, (0, 0, 0), b1, b2, 2)
pygame.draw.line(screen, (0, 0, 0), b3, b2, 2)
pygame.draw.line(screen, (0, 0, 0), b3, a2, 2)
pygame.draw.line(screen, (0, 0, 0), b1, a2, 2)

pygame.draw.line(screen, (0, 0, 0), a1, c1, 2)
pygame.draw.line(screen, (0, 0, 0), c1, c2, 2)
pygame.draw.line(screen, (0, 0, 0), b1, c2, 2)

pygame.draw.line(screen, (0, 0, 0), b1, d1, 2)
pygame.draw.line(screen, (0, 0, 0), d1, d2, 2)
pygame.draw.line(screen, (0, 0, 0), d3, d2, 2)
pygame.draw.line(screen, (0, 0, 0), b1, d3, 2)

pygame.draw.line(screen, (0, 0, 0), d1, a3, 2)
pygame.draw.line(screen, (0, 0, 0), a1, a3, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

