import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Bisect given circumfrence

a = (300, 300)
b = (300, 200)
c = (200, 300)
d = (400, 300)

e = 100


pygame.draw.line(screen, (0, 0, 0), b, c, 2)
pygame.draw.line(screen, (0, 0, 0), b, d, 2)
pygame.draw.line(screen, (0, 0, 0), a, b, 2)

pygame.draw.circle(screen, (0, 0, 0), a, e, 2)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
