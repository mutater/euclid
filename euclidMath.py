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
