import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# point not taken on the center of the circle will have, you guessed it, unequal lines touching the edge of the circle

a = (300, 300)
b = (350, 300)
c = (400, 300)
d = (200, 300)

distAC = 100

pygame.draw.line(screen, (0, 0, 0), c, d, 2)
pygame.draw.line(screen, (0, 0, 0), b, (300, 200), 2)

pygame.draw.circle(screen, (0, 0, 0), a, distAC, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

