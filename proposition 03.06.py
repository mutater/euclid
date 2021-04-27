import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# If two circles touch at a single point, they do not have the same centre.

a = (300, 300)
b = (325, 300)

c = 100
d = 75

pygame.draw.circle(screen, (0, 0, 0), a, c, 1)
pygame.draw.circle(screen, (0, 0, 0), b, d, 1)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

