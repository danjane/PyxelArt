import pyxel
import numpy as np
import math

W = 1600
SEGMENTS = 1000
LINES = 80

def vector(cs):
    return np.array(cs)


def bezier_point(t, control_points):
    """ Calculate the position of a point on the Bezier curve at parameter t """
    n = len(control_points) - 1
    p = vector([0., 0.])
    # Calculate point on the Bezier curve using the Bernstein polynomial
    for i, point in enumerate(control_points):
        binomial_coeff = math.comb(n, i)
        p += binomial_coeff * (t ** i) * ((1 - t) ** (n - i)) * point
    return p


def bezier_points(control_points, segments=SEGMENTS):
    """ Draw a Bezier curve based on given control points """
    vs = [vector(v) for v in control_points]
    points = []
    for i in range(segments + 1):
        t = i / segments
        points.append(bezier_point(t, vs))
    return points


def lines(points, colour):
    for p in points:
        pyxel.circ(*p, 4, colour)


pyxel.init(W, W)
pyxel.cls(0)
pyxel.colors[0] = 0xdddddd
pyxel.colors[7] = 0x123456

ys_unscaled = []
for _ in range(LINES//2):
    ys_unscaled.append(1.4)
for _ in range(LINES // 2):
    ys_unscaled.append(1)
ys_unscaled = ys_unscaled[:LINES]

ys = [W*y/sum(ys_unscaled) for y in ys_unscaled]

y1 = 0
y2 = 0
for i in range(LINES):
    ps = bezier_points([[0, y1], [W/2, y1], [W/2, y2], [W, y2]])
    lines(ps, pyxel.rndi(1, 15))
    y1 = y1 + ys[i]
    y2 = y2 + ys[-i-1]

pyxel.show()