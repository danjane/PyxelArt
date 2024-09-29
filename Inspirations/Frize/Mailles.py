import pyxel
import numpy as np

W = 1600
SEGMENTS = 1000
LINES = 80

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
        pyxel.circ(*p, 4, couleur)

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
    ps = [[0, y1], [W/2, y1], [W/2, y2], [W, y2]]
    trace(ps, pyxel.rndi(1, 15))
    y1 = y1 + ys[i]
    y2 = y2 + ys[-i-1]

pyxel.show()