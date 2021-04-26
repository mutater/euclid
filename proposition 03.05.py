import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# If two circles intersect anywhere, they do not have the same centre

a = (300, 300)
b = (350, 350)

c = 100

pygame.draw.circle(screen, (0, 0, 0), a, c, 2)
pygame.draw.circle(screen, (0, 0, 0), b, c, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

