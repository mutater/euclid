import sys, pygame
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((900, 600))

screen.fill((0, 0, 0))

#out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manner
#should be greater than the remaining one

lA = 100
lB = 200
#lC = 10, just KIDDING NIGGA, FUCK YOU, l stands for length

a = (400, 200)
b = (200, 300)
c = (400, 300)
#c doesn't exist, it's just a place holder bc there's no fucktion for meeting at 90 degree angle
lC = Math.pythag(a, b)

eA = (600, 250)
eB = (600, 300)
eC = (600, 350)
fA = (600 + lA, 250)
fB = (600 + lB, 300)
fC = (600 + lC, 350)


pygame.draw.line(screen, (255, 255, 255), a, b, 2)
pygame.draw.line(screen, (255, 255, 255), a, c, 2)
pygame.draw.line(screen, (255, 255, 255), b, c, 2)


pygame.draw.line(screen, (255, 255, 255), eA, fA, 2)
pygame.draw.line(screen, (255, 255, 255), eB, fB, 2)
pygame.draw.line(screen, (255, 255, 255), eC, fC, 2)

pygame.draw.circle(screen, (255, 255, 255), c, lA, 2)
pygame.draw.circle(screen, (255, 255, 255), b, lC, 2)

pygame.display.flip()
input()