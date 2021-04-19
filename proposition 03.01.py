import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# To find the center* of a cricle

a = (250, 350)
b = (350, 350)

c = (300, 300)
distCB = Math.distance(a[0], c[0], a[1], c[1])

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), (300, 600), (300, 0), 2)

pygame.draw.circle(screen, (0, 0, 0), c, distCB, 2)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

