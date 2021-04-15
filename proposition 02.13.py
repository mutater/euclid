import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# The square on the acute angle of an acute triangle is equal to the other 2 squares - 2 times the rectangle contained by the longest side.

a = (200, 300)
b = (400, 300)
c = (300, 200)

d = (100, 200)
e = (200, 100)

f = (500, 200)
g = (400, 100)

h = (200, 500)
i = (400, 500)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)

pygame.draw.line(screen, (0, 0, 0), a, d, 2)
pygame.draw.line(screen, (0, 0, 0), d, e, 2)
pygame.draw.line(screen, (0, 0, 0), c, e, 2)

pygame.draw.line(screen, (0, 0, 0), f, b, 2)
pygame.draw.line(screen, (0, 0, 0), f, g, 2)
pygame.draw.line(screen, (0, 0, 0), c, g, 2)

pygame.draw.line(screen, (0, 0, 0), a, h, 2)
pygame.draw.line(screen, (0, 0, 0), h, i, 2)
pygame.draw.line(screen, (0, 0, 0), i, b, 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


