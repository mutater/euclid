import sys, pygame, math
from pygame.locals import *
from euclidMath import Math
pygame.init()

screen = pygame.display.set_mode((1000 ,1000))

Math = Math()


# To bisect a given rectilineal angle

a = (400, 200)
b = (678, 449)
c = (a[0]-b[0]+a[0], 449)

distBC = Math.distance(c[0], c[1], b[0], b[1])
sqrtisgay = Math.pythagac(distBC/2, distBC)

d = (a[0], sqrtisgay + b[1])

# screen fill

screen.fill((255, 255, 255))

# Triangle cunstruction

pygame.draw.line(screen, (0, 0, 0), a, b, 2)
pygame.draw.line(screen, (0, 0, 0), c, b, 2)
pygame.draw.line(screen, (0, 0, 0), a, c, 2)

# prop 2 on line bc

pygame.draw.line(screen, (0, 0, 0), b, d, 1)
pygame.draw.line(screen, (0, 0, 0), d, c, 1)

# Bisector

pygame.draw.line(screen, (0, 0, 0), a, d, 2)

pygame.display.flip()
input()