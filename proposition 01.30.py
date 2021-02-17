import sys, pygmame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Straight lines paralelel t the same straight line are also parallel to one another

a = (100, 200)
b = (500, 200)

c = (100, 350)
d = (500, 350)

e = (100, 500)
f = (100, 500)

g = (50, 550)
h = (550, 50)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)
pygame.draw.line(screen, (0, 0, 0), e, f, 2)
pygame.draw.line(screen, (0, 0, 0), g, h, 2)

pygame.display.flip()

input()