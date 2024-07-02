import pyxel

pyxel.init(500, 750)
pyxel.cls(7)

dn1 = 550
dn = 750
for _ in range(15):
    pyxel.line(0, dn1+100, pyxel.width, dn1+100, 0)
    dn, dn1 = dn1, dn1**2/dn

pyxel.rect(249, 0, 2, 300, 10)
pyxel.circ(250, 300, 150, 1)

pyxel.show()