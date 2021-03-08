import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# To construct, in a given rectilineal angle, a parallelogram equal to a given triangle

a = (200, 200)
b = (225, 300)
c = (425, 300)
d = (400, 200)

e = (375, 300)
f = (350, 200)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)

pygame.draw.line(screen, (0, 0, 0), a, c, 2)

pygame.draw.line(screen, (0, 0, 0), e, f, 2)

pygame.display.flip()

input()