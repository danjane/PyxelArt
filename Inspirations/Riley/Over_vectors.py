import pyxel
import numpy as np
import math

W = 800
SEGMENTS = 1000


def rot90(v):
    return np.array([-v[1], v[0]])


def norm(v):
    return (v[0] ** 2 + v[1] ** 2) ** 0.5


def bezier_point(t, control_points):
    """ Calculate the position of a point on the Bezier curve at parameter t """
    n = len(control_points) - 1
    p = np.zeros(2)
    # Calculate point on the Bezier curve using the Bernstein polynomial
    for i, point in enumerate(control_points):
        binomial_coeff = math.comb(n, i)
        p += binomial_coeff * (t ** i) * ((1 - t) ** (n - i)) * point
    return p


def bezier_points(control_points, segments=SEGMENTS):
    """ Draw a Bezier curve based on given control points """
    vs = [np.array(v) for v in control_points]
    points = []
    for i in range(segments + 1):
        t = i / segments
        points.append(bezier_point(t, vs))
    return points


def parallels(vectors, offsets):
    for i in range(len(vectors) - 1):
        a = vectors[i]
        b = vectors[i + 1]

        m = (a + b) / 2

        c = b - a
        n = rot90(c)
        n = n / norm(n)

        for d in offsets:
            p = m + d * n
            pyxel.circ(*p, 3, 1)


pyxel.init(W, W)
pyxel.colors[0] = 0x555555
pyxel.colors[1] = 0xcccccc

ps = bezier_points([(W, 0), (W / 3, 0), (2 * W / 3, W), (0, W)])
parallels(ps, range(-W, W, 15))

pyxel.show()
