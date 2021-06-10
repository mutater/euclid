import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# two different circles cannot be drawn on the same line

a = (200, 300)
b = (400, 300)
c = (300, 300)
d = 100
e = (300, 400)
f = 200

pygame.draw.line(screen, (0, 0, 0), a, b, 2)

pygame.draw.circle(screen, (0, 0, 0), c, d, 2)
pygame.draw.circle(screen, (0, 0, 0), e, f, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
