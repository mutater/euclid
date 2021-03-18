import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

# Pythagorean therom but opposite (Instead of getting the hypotenuse's length we prove that the angle opposite the hypotenuse is right because the two squares of the adjacent lines add up to the square of the hypotenuse)

a = (200, 300)
b = (400, 300)
c = (300, 200)

d = (100, 200)
e = (200, 100)

f = (500, 200)
g = (400, 100)

h = (200, 500)
i = (400, 500)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)

pygame.draw.line(screen, (0, 0, 0), a, d, 2)
pygame.draw.line(screen, (0, 0, 0), d, e, 2)
pygame.draw.line(screen, (0, 0, 0), c, e, 2)

pygame.draw.line(screen, (0, 0, 0), f, b, 2)
pygame.draw.line(screen, (0, 0, 0), f, g, 2)
pygame.draw.line(screen, (0, 0, 0), c, g, 2)

pygame.draw.line(screen, (0, 0, 0), a, h, 2)
pygame.draw.line(screen, (0, 0, 0), h, i, 2)
pygame.draw.line(screen, (0, 0, 0), i, b, 2)

pygame.display.flip()

input()