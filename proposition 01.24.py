import sys, pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# If two triangle have the two sides equal to two sides respectively, but have the one of the angles contained by the equal straight lines greater that the other,
# they will also have the base greater than the base

a = (200, 100)
b = (130, 120)
c = (270, 140)

d = (400, 100)
e = (350, 140)
f = (450, 160)

# angle A is greater than angle D eez nuts hah goteem

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), d, e, 2)
pygame.draw.line(screen, (0, 0, 0), d, f, 2)
pygame.draw.line(screen, (0, 0, 0), e, f, 2)


pygame.display.flip()

input()