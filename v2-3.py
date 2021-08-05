from veuclid import *

# - Identity
# If a straight line is cut, the rectangle contained by the whole and one of the segments is equal to the sum of the
# the rectangle contained by the segments and the square on the aforementioned segment

# - Drawing

# Let the straight line AB be cut at random at the point C

point_a = Point(200, 200)
point_b = Point(600, 200)

line_ab = Line(point_a, point_b)

point_c = line_ab.get_point_on_line()

# Let the square CDEB be described on CB

line_bc = Line(point_b, point_c)

line_cd = Line(point_c, line_bc.slope.get_perpendicular(), line_bc.length)
line_be = Line(point_b, line_bc.slope.get_perpendicular(), line_bc.length)

point_d = line_cd.end
point_e = line_be.end

line_de = Line(point_d, point_e)

# Let ED be drawn through to F, and through A let AF be drawn parallel to either CD or BE

line_af = Line(point_a, line_ab.slope.get_perpendicular(), line_cd.length)

point_f = line_af.end

line_df = Line(point_d, point_f)

wait()
