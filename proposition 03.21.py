import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#angles made from the same line will be equal.

a = (300, 300)
b = (235, 372)
c = (365, 372)
d = (200, 300)
e = (323, 203)

f = 100

pygame.draw.circle(screen, (0, 0, 0), a, f, 2)

pygame.draw.line(screen, (0, 0, 0), b, c, 2)

pygame.draw.line(screen, (0, 0, 0), b, d, 2)
pygame.draw.line(screen, (0, 0, 0), d, c, 2)

pygame.draw.line(screen, (0, 0, 0), b, e, 2)
pygame.draw.line(screen, (0, 0, 0), e, c, 2)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
