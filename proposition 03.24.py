import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Similar segments of circles on equal lines are equal

a = (100, 300)
b = (250, 300)
c = (350, 300)
d = (500, 300)

e = (175, 300)
f = (425, 300)

g = 75

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)

pygame.draw.circle(screen, (0, 0, 0), e, g, 2)
pygame.draw.circle(screen, (0, 0, 0), f, g, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
