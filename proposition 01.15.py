import pygame, sys
from euclidMath import Math
from pygame.locals import *
pygame.init

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#If two straight lines cut one another, they make the vertical angles equal to one another

pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 400), 2)
pygame.draw.line(screen, (0, 0, 0), (0, 300), (600, 300), 2)

pygame.display.flip()
input()