import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# If a point inside a circle has more than two equal straight lines drawn to it, then it is the centre of the circle.

a = (300, 300)
b = (400, 300)
c = (300, 400)
d = (325, 325)
e = (300, 200)

pygame.draw.line(screen, (0, 0, 0), a, b, 1)
pygame.draw.line(screen, (0, 0, 0), c, a, 1)
pygame.draw.line(screen, (0, 0, 0), c, d, 1)
pygame.draw.line(screen, (0, 0, 0), b, d, 1)

pygame.draw.line(screen, (0, 0, 0), a, e, 2)
pygame.draw.line(screen, (0, 0, 0), e, d, 2)

pygame.draw.circle(screen, (0, 0, 0), a, 100, 1)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

