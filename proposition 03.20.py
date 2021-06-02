import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# A right angle will always be adjacent to the tangent line, coming from the centre

a = (300, 300)
b = (400, 100)
c = (400, 500)
d = (400, 300)
e = (200, 300)

f = 100

pygame.draw.circle(screen, (0, 0, 0), a, f, 2)

pygame.draw.line(screen, (0, 0, 0), b, c, 2)
pygame.draw.line(screen, (0, 0, 0), e, d, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
