import pyxel

W = 800
F = 0.8
N = 25

pyxel.init(W, W)
pyxel.colors[0] = 0xeecea5
pyxel.colors[1] = 0x927d5e


def line(*xys):
    def scale(x):
        return (x * F + 1) * W / 2

    pyxel.line(*[scale(xy) for xy in xys], 1)


def c(z):
    return pyxel.cos(z * 360 / N)


def s(z):
    return pyxel.sin(z * 360 / N)


for i in range(N):
    for j in range(i + N // 2 - 9, i + N // 2 + 9):
        line(c(i), s(i), c(j), s(j))

pyxel.show()
