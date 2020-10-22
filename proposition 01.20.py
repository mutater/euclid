import pygame, sys
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#In any triangle two sides taken together in any manner are greater than the remaining one


a = (200, 200)
b = (a[0]-1, a[1]+50)
c = (a[0], a[1]+100)


pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)


pygame.display.flip()

input()