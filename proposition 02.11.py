import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# A small rectangle equals a square

a = (200, 200)
b = (300, 200)
c = (200, 300)
d = (300, 300)

e = (200, 250)
distEB = Math.distance(e[0], e[1], b[0], b[1])

f = (200, 250-distEB)
g = (200 + distEB, 250 - distEB)
h = (200 + distEB, 300)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)

pygame.draw.line(screen, (0, 0, 0), e, b, 2)

pygame.draw.line(screen, (0, 0, 0), a, f, 2)
pygame.draw.line(screen, (0, 0, 0), f, g, 2)
pygame.draw.line(screen, (0, 0, 0), g, h, 2)

pygame.draw.circle(screen, (0, 0, 0), e, distEB, 1)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


