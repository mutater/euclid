import sys, pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# proposition 01.35 but there's more parallelograms (1 MORE)

a = (100, 200)
b = (150, 300)
c = (200, 300)
d = (150, 200)

e = (300, 200)
f = (350, 200)
g = (400, 300)
h = (450, 300)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), d, c, 2)
pygame.draw.line(screen, (0, 0, 0), a, d, 2)

pygame.draw.line(screen, (0, 0, 0), e, b, 2)
pygame.draw.line(screen, (0, 0, 0), f, c, 2)
pygame.draw.line(screen, (0, 0, 0), e, f, 2)

pygame.draw.line(screen, (0, 0, 0), e, g, 2)
pygame.draw.line(screen, (0, 0, 0), h, f, 2)
pygame.draw.line(screen, (0, 0, 0), h, g, 2)


pygame.display.flip()

input()