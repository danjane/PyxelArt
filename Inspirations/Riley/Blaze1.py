import pyxel

W = 800
SEGMENTS = 100
OFFSET = 10
RADII = 20
N_CIRCLES = 15
CENTRE_SHIFTS = 0.6

pyxel.init(W, W)
pyxel.colors[1] = 0x555555
pyxel.colors[0] = 0xcccccc
pyxel.cls(0)


def quad(a1, a2, a3, a4):
    pyxel.tri(*a1, *a2, *a3, 1)
    pyxel.tri(*a2, *a3, *a4, 1)


centres = [[W / 2, W / 2]]
for _ in range(N_CIRCLES - 1):
    x, y = centres[-1]
    m = RADII * CENTRE_SHIFTS
    centres.append([x + pyxel.rndf(-m, m), y + pyxel.rndf(-m, m)])

thetas = []
for i in range(SEGMENTS):
    thetas.append(360 * i / SEGMENTS)
thetas.append(thetas[0])

offset = 0
circles = []
r = 3 * RADII
for x, y in centres:
    r = r + RADII
    points = []
    offset = OFFSET - offset
    for theta in thetas:
        points.append([x + r * pyxel.cos(theta + offset), y + r * pyxel.sin(theta + offset)])
    circles.append(points)

for c in range(N_CIRCLES - 1):
    for i in range(0, SEGMENTS, 2):
        p = circles[c][i]
        q = circles[c][i + 1]
        r = circles[c + 1][i]
        s = circles[c + 1][i + 1]
        quad(p, q, r, s)

pyxel.show()
