import pyxel

pyxel.init(600, 1000)

shift = 0
pyxel.cls(8)
for y in range(0, pyxel.height, 20):
    radius = int((y / pyxel.height) * 15) + 1
    shift = (shift + 1) % 2
    for x in range(0, pyxel.width + 10, 20):
        pyxel.circ(x + 10 * shift, y, radius, 10)


def concentric_circles(x, y, r_max, step):
    colours = [7, 0]
    idx = 0
    for r in range(r_max, 1, -step):
        pyxel.circ(x, y, r, colours[idx])
        idx = (idx+1) % len(colours)

concentric_circles(400, 500, 125, 10)


pyxel.show()
