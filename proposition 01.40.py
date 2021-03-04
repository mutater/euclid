import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Using propositions written before it can be proven that with two equal triangles sharing the same base have the base parallel
# to the line that extends from the top of one triangle to the other

a = (234, 200)
b = (175, 300)
c = (425, 300)
d = (400, 200)
e = (300, 300)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)

pygame.draw.line(screen, (0, 0, 0), a, e, 2)
pygame.draw.line(screen, (0, 0, 0), e, d, 2)

pygame.display.flip()

input()