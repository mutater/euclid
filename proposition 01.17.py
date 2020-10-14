import sys, pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))

screen.fill((255, 255, 255))

#In any triangle two angles taken together in any manner are less than two right angles. 

pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), 2)
pygame.draw.line(screen, (0, 0, 0), (0, 200), (400, 600), 2)
pygame.draw.line(screen, (0, 0, 0), (0, 300), (600, 500), 2)

pygame.display.flip()
input()