import math
import pygame
import random
import sys

pygame.init()
pygame.display.set_caption("Euclids")
screen = pygame.display.set_mode((800, 800))
screen.fill((255, 255, 255))
random.seed()


def distance(*args):
    if type(args[0]) is Line:
        start = Line.start.get_pos()
        end = Line.end.get_pos()
    else:
        if type(args[0]) is list:
            start = args[0]
        elif type(args[0]) is Point:
            start = args[0].get_pos()
        else:
            start = [0, 0]
        
        if type(args[1]) is list:
            end = args[1]
        elif type(args[1]) is Point:
            end = args[1].get_pos()
        else:
            start = [1, 1]
    
    return math.sqrt(((end[0] - start[0]) ** 2) + ((end[1] - start[1]) ** 2))


def slope(*args):
    if type(args[0]) is Line:
        start = args[0].start.get_pos()
        end = args[0].end.get_pos()
    else:
        if type(args[0]) is list:
            start = args[0]
        elif type(args[0]) is Point:
            start = args[0].get_pos()
        else:
            start = [0, 0]
        
        if type(args[1]) is list:
            end = args[1]
        elif type(args[1]) is Point:
            end = args[1].get_pos()
        else:
            start = [1, 1]
    
    if (end[0] - start[0]) == 0:
        return "n/a"
    else:
        return (end[1] - start[1]) / (end[0] - start[0])


def line_intersection(*args):
    line1 = args[0]
    line2 = args[1]
    
    if line1.slope.angle == line2.slope.angle:
        return
    
    def determinate(a, b, c, d):
        return a * d - b * c
    
    x1 = line1.start.get_x()
    x2 = line1.end.get_x()
    x3 = line2.start.get_x()
    x4 = line2.end.get_x()
    y1 = line1.start.get_y()
    y2 = line1.end.get_y()
    y3 = line2.start.get_y()
    y4 = line2.end.get_y()
    
    denominator = determinate(
        x1 - x2, 
        y1 - y2,
        x3 - x4,
        y3 - y4
    )
    
    x = determinate(
        x1 * y2 - y1 * x2,
        x1 - x2,
        x3 * y4 - y3 * x4,
        x3 - x4
    )
    
    y = determinate(
        x1 * y2 - y1 * x2,
        y1 - y2,
        x3 * y4 - y3 * x4,
        y3 - y4
    )
    
    return Point(x / denominator, y / denominator)


class Point:
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            self.pos = [args[0], args[1]]
        else:
            self.pos = args[0]
        
        self.width = kwargs.get("width", 2)
        
        if kwargs.get("show", True):
            self.draw()
    
    def draw(self):
        pygame.draw.circle(screen, (0, 0, 0), (self.pos[0] + 1, self.pos[1] + 1), self.width)
    
    def get_pos(self):
        return [round(self.pos[0]), round(self.pos[1])]
    
    def get_x(self):
        return round(self.pos[0])
    
    def get_y(self):
        return round(self.pos[1])


class Slope:
    def __init__(self, *args):
        self.angle = args[0]
    
    def get_end_pos(self, start, length, negative=True, show=True):
        if type(start) is Point:
            start = start.get_pos()
        
        if self.angle == 0:
            return Point([start[0] + length, start[1]], show=show)
        elif self.angle == "n/a":
            return Point([start[0], start[1] + length], show=show)
        else:
            k = length * 1 / math.sqrt(1 + self.angle ** 2)
            xd = k * (-1 if negative else 1)
            yd = self.angle * k * (-1 if negative else 1)
            
            return Point([start[0] + xd, start[1] + yd], show=show)
    
    def get_perpendicular(self):
        if self.angle == 0:
            return Slope("n/a")
        elif self.angle == "n/a":
            return Slope(0)
        else:
            return Slope(-1 / self.angle)


class Line:
    def __init__(self, *args, **kwargs):
        if type(args[0]) is list:
            self.start = Point(args[0], show=kwargs.get("show", True))
        elif type(args[0]) is Point:
            self.start = args[0]
        else:
            self.start = [0, 0]
        
        if type(args[1]) is list:
            self.end = Point(args[1], show=kwargs.get("show", True))
        elif type(args[1]) is Point:
            self.end = args[1]
        elif type(args[1]) is Slope:
            self.end = args[1].get_end_pos(self.start, args[2], show=kwargs.get("show", True))
        else:
            self.end = [0, 0]
        
        if type(args[1]) is Slope and len(args) > 2:
            self.slope = args[1]
            self.length = args[2]
        else:
            self.slope = Slope(slope(self))
            self.length = distance(self.start, self.end)
        
        self.width = kwargs.get("width", 1)
        
        if kwargs.get("show", True):
            self.draw()
    
    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), self.start.get_pos(), self.end.get_pos(), self.width)
    
    def cut(self, length):
        return self.slope.get_end_pos(self.start, length)
    
    def get_point_on_line(self):
        random_length = random.randint(0, math.floor(self.length))
        
        return self.slope.get_end_pos(self.start, random_length, negative=False)


def wait():
    pygame.display.update()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
