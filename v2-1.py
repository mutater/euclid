from veuclid import *

# - Identity
# If one straight line of two is cut into a number of segments, the rectangle contained by the two straight lines is
# equal to the sum of the rectangles contained by the uncut straight line and each of the segments.

# - Drawing

# Let A, BC be two straight lines, and let BC be cut at random at the points D, E

line_a = Line([200, 100], [400, 100])

point_b = Point(200, 200)
point_c = Point(600, 200)

line_bc = Line(point_b, point_c)

point_d = line_bc.get_point_on_line()

line_dc = Line(point_d, point_c)

point_e = line_dc.get_point_on_line()

# Let BF be drawn from B at right angles to BC; let BG be made equal to A

line_bf = Line(point_b, line_bc.slope.get_perpendicular(), line_a.length + 20)
line_bg = Line(point_b, line_bf.cut(line_a.length))

point_f = line_bf.end
point_g = line_bg.end

# Through G let GH be drawn parallel to BC

line_gh = Line(point_g, line_bc.slope, line_bc.length)

point_h = line_gh.end

# Through D, E, C let DK, EL, CH be drawn parallel to BG

line_d_ext = Line(point_d, line_bc.slope.get_perpendicular(), line_bf.length, show=False)
line_e_ext = Line(point_e, line_bc.slope.get_perpendicular(), line_bf.length, show=False)

point_k = line_intersection(line_gh, line_d_ext)
point_l = line_intersection(line_gh, line_e_ext)

line_dk = Line(point_d, point_k)
line_el = Line(point_e, point_l)
line_gh = Line(point_c, point_h)

wait()
