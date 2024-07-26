import pyxel

N = 50
F = 0.8
W = 800

pyxel.init(W, W)
pyxel.colors[0] = 0xeecea5
pyxel.colors[1] = 0x927d5e


def line(*xys):
    def scale(x):
        return (x * F + 1) * W / 2

    pyxel.line(*[scale(xy) for xy in xys], 1)


pyxel.rectb((1 - F) * W / 2, (1 - F) * W / 2, F * W, F * W, 1)

for i in range(N):
    a = i / N
    b = 1 - a
    for r in [-1, 1]:
        for s in [-1, 1]:
            line(r * a, s * a, 0, s * b)
            line(s * a, r * a, s * b, 0)

pyxel.rectb(F * W, F * W, (1 - 2 * F) * W, (1 - 2 * F) * W, 1)

pyxel.show()
