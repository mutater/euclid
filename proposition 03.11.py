import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# If a circle inside another circle touches the inside of said circle, a line produced from the middles of both circles will cut through the point of contact between circles

a = (300, 300)
b = (275, 275)

c = 100
d = 65

pygame.draw.circle(screen, (0, 0, 0), a, c, 2)
pygame.draw.circle(screen, (0, 0, 0), b, d, 2)

pygame.draw.line(screen, (0, 0, 0), a, (0, 0), 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

