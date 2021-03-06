import math


class Math():
    def distance(self, x1, y1, x2, y2):
        sqrt1 = (x1-x2)*(x1-x2)
        sqrt2 = (y1-y2)*(y1-y2)
        return int(math.sqrt(sqrt1 + sqrt2))

    def pythagac(self, a, c):
        return int(math.sqrt(c**2 - a**2))

    def avg(self, x, y):
        return int((x + y)/2)

    def vardist(self, c, d):
        sqrt3 = abs(c[0]-c[1])*(c[0]-c[1])
        sqrt4 = abs(d[0]-d[1])*(d[0]-d[1])
        return int(math.sqrt(sqrt3 + sqrt4))
        
    def pythag(self, a, b):
        abX = (abs(a[0]-b[0]))
        abY = (abs(a[1]-b[1]))
        
        return int(math.sqrt(abX**2 + abY**2))