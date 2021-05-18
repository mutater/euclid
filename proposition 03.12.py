import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Same thing as last time but the circle inside is outside

a = (300, 300)
b = (185, 185)

c = 100
d = 65

pygame.draw.circle(screen, (0, 0, 0), a, c, 2)
pygame.draw.circle(screen, (0, 0, 0), b, d, 2)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

