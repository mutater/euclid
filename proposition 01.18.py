import sys, pygame
from pygame.locals import *
from euclidMath import Math
pygame.init()

Math = Math()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#In any triangle the gerater side subtends the greater angle.

a = (245, 130)
b = (245, 432)
c = (434, 259)
distBC = Math.vardist(b, c)
d = (a[0], b[1]-distBC)

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)
pygame.draw.line(screen, (0, 0, 0), c, d, 2)


pygame.draw.circle(screen, (0, 0, 0), b, distBC, 1)


pygame.display.flip()
input()