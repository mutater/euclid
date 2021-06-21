import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Given a segment of a circle, to give the circle of which the segment is a part of

a = (300, 300)
b = (200, 300)
c = (250, 220)
d = (250, 380)

e = 100

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)

pygame.draw.circle(screen, (0, 0, 0), a, e, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
