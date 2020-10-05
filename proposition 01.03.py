import pygame, sys, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((800, 800))

Math = Math()

# Given two unequal straight lines, to cut off from the greater a straigh line equal to the less.

a = (350, 420)
b = (690, 420)
c = (10, 20)
C = (200, 20)

distcC = Math.distance(c[0], c[1], C[0], C[1])

# Fill screen with white.

screen.fill((255, 255, 255))

# Let AB, C be the two given unequal straight lines, and let AB be the greater of them.

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, C, 2)

# At the point A let AD be placed equal to the straight line C.

pygame.draw.line(screen, (0, 0, 0), a, (a[0], a[1]-distcC), 2)

# With the centre A and distance AD let the circle DEF be described.

pygame.draw.circle(screen, (0, 0, 0), a, distcC, 1)

pygame.display.flip()
input()