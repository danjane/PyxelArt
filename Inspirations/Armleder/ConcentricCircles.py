import pyxel

pyxel.init(1500, 500)
pyxel.colors[0] = 0xffffff
pyxel.colors[1] = 0x0
pyxel.colors[2] = 0xaa0000
centres = []
for i in range(0, 1500, 175):
    centres.append([i, 250])

pyxel.cls(0)

c = 1
for r in range(250, 0, -20):
    c = 3 - c
    for x, y in centres:
        pyxel.circ(x, y, r, c)

    for x, y in centres:
        pyxel.circ(x, y, r-5, 0)


pyxel.show()