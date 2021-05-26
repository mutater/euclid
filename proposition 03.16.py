import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# A straight line drawn at a right angle at the extremity of a diameter will fall outside the circle

a = (300, 300)
b = (300, 400)
c = (300, 200)
d = (100, 400)


f = 100

pygame.draw.circle(screen, (0, 0, 0), a, f, 2)

pygame.draw.line(screen, (0, 0, 0), b, d, 2)
pygame.draw.line(screen, (0, 0, 0), b, c, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

