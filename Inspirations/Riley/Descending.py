import pyxel

W = 800
LINES = 20
SEGMENTS = 100
OFFSET = -50
SHIFT = 2.5

pyxel.init(W, W)
pyxel.colors[1] = 0x555555
pyxel.colors[0] = 0xcccccc
pyxel.cls(0)


def quad(a1, a2, a3, a4):
    pyxel.tri(*a1, *a2, *a3, 1)
    pyxel.tri(*a2, *a3, *a4, 1)


def f(x, y):
    return SHIFT*W/LINES/(3+((y-x)/100)**2)


xs = []
for i in range(LINES+1):
    xs.append(i*W/LINES)

ys = []
for i in range(SEGMENTS+1):
    ys.append(i*W/SEGMENTS)

lines = []
flag = True
for x in xs:
    if flag:
        lines.append([(x, y + OFFSET) for y in ys])
    else:
        lines.append([(x+f(x, y), y) for y in ys])
    flag = not flag

for i in range(LINES):
    for j in range(0, SEGMENTS, 2):
        p = lines[i][j]
        q = lines[i][j+1]
        r = lines[i+1][j]
        s = lines[i+1][j+1]
        quad(p, q, r, s)

pyxel.show()
