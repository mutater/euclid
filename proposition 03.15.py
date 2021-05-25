import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#The diameter of a circle is the greatest, and then the line closest to the diameter, so on so forth

a = (300, 300)
b = (300, 200)
c = (365, 228)
d = (300, 400)
e = (365, 372)

f = 100

pygame.draw.circle(screen, (0, 0, 0), a, f, 2)

pygame.draw.line(screen, (0, 0, 0), c, e, 2)
pygame.draw.line(screen, (0, 0, 0), b, d, 2)


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

