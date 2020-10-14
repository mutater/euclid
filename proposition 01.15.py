import pygame, sys, math
from euclidMath import Math
from pygame.locals import *
pygame.init
from math import *

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#If two straight lines cut one another, they make the vertical angles equal to one another (I now hate this proposition)


e = (129, 12)
justathingiguess = 100/e[0]

distLine = sqrt(100**2 + e[0]**2)
a = e[0]
b = distLine
c = 100
angleUpLeft = acos(((a**2 + b**2) - c**2) / (2 * a * b))
angleUpRight = 180 - angleUpLeft
angleDownRight = angleUpLeft
angleDownLeft = angleUpRight


pygame.draw.line(screen, (0, 0, 0), (0, e[1]), (600, e[1]), 2)
pygame.draw.line(screen, (0, 0, 0), (e[0]*-9, e[1]-(100*10)), (e[0]*11, e[1]+(100*10)), 2)


pygame.display.flip()
input()