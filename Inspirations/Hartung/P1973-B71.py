import pyxel
import numpy as np
import math

W = 800
SEGMENTS = 200

pyxel.init(W, W)
# pyxel.colors[1] = 0x555555
# pyxel.colors[0] = 0xcccccc
pyxel.cls(10)


def vector(components):
    return np.array(components)


def rot90(v):
    return np.array([-v[1], v[0]])


def norm(v):
    return (v[0] ** 2 + v[1] ** 2) ** 0.5


def bezier_point(t, control_points):
    """ Calculate the position of a point on the Bézier curve at parameter t """
    n = len(control_points) - 1
    p = vector([0., 0.])
    # Calculate point on the Bézier curve using the Bernstein polynomial
    for i, point in enumerate(control_points):
        binomial_coeff = math.comb(n, i)
        p += binomial_coeff * (t ** i) * ((1 - t) ** (n - i)) * point
    return p


def bezier_points(control_points, segments=SEGMENTS):
    """ Draw a Bézier curve based on given control points """
    vs = [vector(cs) for cs in control_points]
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
        temp = norm(n)
        if temp > 0:
            n = n / temp
        else:
            continue

        for d in offsets:
            p = m + d * n
            pyxel.circ(*p, 3, 1)


def brighten(cx, cy, colour):
    W2 = (W // 4) ** 2
    for x in range(W):
        for y in range(W):
            r2 = (cx - x) ** 2 + (cy - y) ** 2
            if r2 > W2:
                continue
            f = 2 ** (-r2 / W / 10)
            if pyxel.rndf(0, 1) < f:
                pyxel.pset(x, y, colour)



for y in range(W // 4, 3 * W // 4, W // 8):
    brighten(W / 2 * pyxel.rndf(0.9, 1.1), y, 3)

brighten(W // 2, W // 4, 10)

for y in range(W // 4, W // 2, W // 6):
    brighten(W / 2 * pyxel.rndf(0.9, 1.1), y, 5)

ps = bezier_points(
        [[W // 4, W], [W // 3, W // 2], [W // 4, 2 * W // 3], [W // 4, W // 2]]
    ) + \
    bezier_points(
        [[W // 4, W // 2], [W // 4, W // 3], [W // 3, W // 4], [W // 2, W // 4]]
    ) + \
    bezier_points(
        [[W // 2, W // 4], [3*W // 4, W // 4], [0.9*3*W // 4, W // 4], [3*W // 4, 1.1*W // 4]]
    )
parallels(ps, range(-80, 240, 40))

pyxel.show()
