import pyxel

pyxel.init(600, 1000)

shift = 0
pyxel.cls(8)
for x in range(pyxel.width):
    for y in range(pyxel.height):
        if pyxel.rndi(0, pyxel.height) < y:
            pyxel.pset(x, y, 10)


def concentric_circles(x, y, r_max, step):
    colours = [7, 0]
    idx = 0
    for r in range(r_max, 1, -step):
        pyxel.circ(x, y, r, colours[idx])
        idx = (idx+1) % len(colours)

concentric_circles(400, 500, 125, 10)

pyxel.show()
