import pyxel
import math


W = 800
N = 40

pyxel.init(W, W)
pyxel.colors[0] = 0x555555
pyxel.colors[1] = 0xcccccc


def bezier_point(t, points):
    """ Calculate the position of a point on the Bezier curve at parameter t """
    n = len(points) - 1
    x, y = 0, 0
    # Calculate point on the Bezier curve using the Bernstein polynomial
    for i, (px, py) in enumerate(points):
        binomial_coeff = math.comb(n, i)
        term = binomial_coeff * ((1 - t) ** (n - i)) * (t ** i)
        x += term * px
        y += term * py
    return x, y

def draw_bezier_curve(points, segments=100):
    """ Draw a Bezier curve based on given control points """
    for i in range(segments):
        t1 = i / segments
        t2 = (i + 1) / segments
        x1, y1 = bezier_point(t1, points)
        x2, y2 = bezier_point(t2, points)
        pyxel.line(x1, y1, x2, y2, 1)


pyxel.cls(0)

draw_bezier_curve([(W, 0), (0, 0), (W, W), (0, W)])

s = pyxel.sin(45/2)*4
for d in range(-W, W, 10):
    draw_bezier_curve([(W, d), (d*s, d), (W+d*s, W+d), (0, W+d)])

pyxel.show()


