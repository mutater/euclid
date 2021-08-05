from veuclid import *

# - Identity
# If a straight line is cut at random, the sum of the rectangles of each segment and the whole will be equal to the
# square of the whole.

# - Drawing

# Let the straight line AB be cut at random at the point C

point_a = Point(200, 200)
point_b = Point(600, 200)

line_ab = Line(point_a, point_b)

point_c = line_ab.get_point_on_line()

# Let the square ADEB be described on AB

line_ad = Line(point_a, line_ab.slope.get_perpendicular(), line_ab.length)
line_be = Line(point_b, line_ab.slope.get_perpendicular(), line_ab.length)

point_d = line_ad.end
point_e = line_be.end

line_de = Line(point_d, point_e)

# Let CF be drawn through C parallel to either AD or BE

line_cf = Line(point_c, line_ad.slope, line_ab.length)

wait()
