import pyxel

W = 800

pyxel.init(W, W)
pyxel.colors[0] = 0x555555
pyxel.colors[1] = 0xcccccc
pyxel.cls(0)

for x in [1, W / 2, W - 1]:
    for y in [1, W / 2, W - 1]:
        for i in range(24):
            theta = i * 360 / 24
            r = pyxel.rndi(0, W // 2)
            pyxel.line(x, y, x + r * pyxel.cos(theta), y + r * pyxel.sin(theta), 1)

pyxel.show()
