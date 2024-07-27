import pyxel

pyxel.init(600, 600)
pyxel.colors[0] = 0xe3e1ec
pyxel.colors[1] = 0x9c011b
pyxel.colors[2] = 0xaf9880

pyxel.cls(0)
for i in range(5):
    for j in range(5):
        if pyxel.rndi(1, 2) == 1:
            r = 20
        else:
            r = 25
        c = pyxel.rndi(1, 2)
        pyxel.circ(100 + i*100, 100+j*100, r, c)

pyxel.show()