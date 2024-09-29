import pyxel
import numpy as np

W = 800
SEGMENTS = 10000

def bezier_point(vec_ctrls, t):
    p = (1-t) ** 3 * vec_ctrls[0] + 3 * (1 - t) ** 2 * t * vec_ctrls[1] + 3 * (1 - t) * t ** 2 * vec_ctrls[2] + t ** 3 * vec_ctrls[3]
    return p

def bezier_points(pt_ctrls):
    vec_ctrls = np.array(pt_ctrls)
    points = []
    for i in range(SEGMENTS + 1):
        t = i / SEGMENTS
        points.append(bezier_point(vec_ctrls, t))
    return points

def trace(pt_ctrls, couleur):
    for p in bezier_points(pt_ctrls):
        pyxel.circ(*p, couleur)

def random_line(x1, y1, x2, y2, colour):
    def b(z, d):
        return z + pyxel.rndf(-0.2, 0.2)*abs(d)

    xd = x2-x1
    yd = y2-y1
    ps = [
        [b(x1, xd), b(y1, yd), 0],
        [b(x1, xd), y1 + 0.5*xd, 10],
        [b(x2, xd), y1 + 0.4*xd, 10],
        [b(x2, xd), b(y2, yd), 0]]
    trace(ps, colour)

pyxel.init(W, 2*W)
pyxel.cls(0)
pyxel.colors[0] = 0xe8e2d2
pyxel.colors[1] = 0x428b67
pyxel.colors[2] = 0x79b1ad
pyxel.colors[3] = 0x928358
pyxel.colors[4] = 0x0f0f0f

# Greens
for i in range(5):
    x = i / 10 + pyxel.rndf(-0.1, 0.1)
    random_line((0.2+x)*W, 1.3*W, (0.1+x)*W, 0.5*W/6, 1)

# Blues
for i in range(5):
    x = i/10+pyxel.rndf(-0.1, 0.1)
    random_line((0.3+x)*W, 1.3*W, (0.6+x)*W, 0.5*W/6, 2)

# Browns
for i in range(3):
    x = i/12+pyxel.rndf(-0.1, 0.1)
    random_line((0.8+x)*W, 1.8*W, (0.75+x)*W, 0.5*W/6, 3)

# Black1
for i in range(20):
    x1 = i / 30 + pyxel.rndf(-0.3, 0.0)
    x2 = i / 30 + pyxel.rndf(-0.1, 0.1)
    random_line((0.1+x1)*W, 1.2*W, (0.2+x2)*W, 0.5*W/6, 4)

pyxel.show()