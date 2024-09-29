import pyxel
import numpy as np

SEGMENTS = 1000

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


pyxel.init(400, 400)

pyxel.colors[0] = 0xAFD6B4
pyxel.colors[1] = 0xf59690

pyxel.cls(0)

points_de_controle = [
    [100, 100, 0],
    [300, 100, 10],
    [100, 300, 10],
    [300, 300, 0]
]

trace(points_de_controle, 1)

pyxel.show()