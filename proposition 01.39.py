import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Equal triangles sharing a common base are parallel

a = (200, 200)
b = (175, 300)
c = (425, 300)
d = (400, 200)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)

pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), d, b, 2)

pygame.display.flip()

input()