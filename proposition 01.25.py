import pygame, sys
from pygame. locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# If two triangles have the two sides equal to two sides respectively, but have the base greater than the base, they will also have the one of the angles
# contained by the equal straight lines greater than the other

a = (200, 300)
b = (130, 320)
c = (270, 340)

d = (400, 300)
e = (350, 340)
f = (450, 360)


pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), b, c, 2)
pygame.draw.line(screen, (0, 0, 0), d, e, 2)
pygame.draw.line(screen, (0, 0, 0), d, f, 2)
pygame.draw.line(screen, (0, 0, 0), e, f, 2)


pygame.display.flip()

input()