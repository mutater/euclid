import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# same as last prop

a = (200, 300)
c = (150, 380)
d = (250, 380)

e = 100

f = (500, 300)
h = (450, 380)
i = (550, 380)

pygame.draw.line(screen, (0, 0, 0), d, c, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)

pygame.draw.circle(screen, (0, 0, 0), a, e, 2)

pygame.draw.line(screen, (0, 0, 0), f, h, 2)
pygame.draw.line(screen, (0, 0, 0), i, h, 2)
pygame.draw.line(screen, (0, 0, 0), i, f, 2)

pygame.draw.circle(screen, (0, 0, 0), f, e, 2)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
