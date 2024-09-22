import pyxel

SEGMENTS = 1000

pyxel.init(400, 400)

pyxel.colors[0] = 0xAFD6B4
pyxel.colors[1] = 0xf59690

pyxel.cls(0)

for i in range(SEGMENTS+1):
    x = 100 + 200 * i/SEGMENTS
    y = 100 + 50  * i/SEGMENTS
    r = 0   + 10  * i/SEGMENTS
    pyxel.circ(x, y, r, 1)

pyxel.show()