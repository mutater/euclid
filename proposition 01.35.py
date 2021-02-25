import sys, pygamne
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Line AB is equal to line BC, and line BC is equal to line EF, so line EF is equal to AB 

a = (100, 200)
b = (150, 300)
c = (200, 300)
d = (150, 200)

e = (300, 200)
f = (350, 200)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), d, c, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)

pygame.draw.line(screen, (0, 0, 0), e, b, 2)
pygame.draw.line(screen, (0, 0, 0), f, c, 2)
pygame.draw.line(screen, (0, 0, 0), e, f, 2)

pygame.display.flip()

input()