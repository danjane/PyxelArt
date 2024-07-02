import pyxel

theta_increment = 1


def xy(a, b, theta, rot):
    t = abs(theta)
    return a * b ** t * pyxel.cos(theta + rot) + pyxel.width / 2,\
           a * b ** t * pyxel.sin(theta + rot) + pyxel.height / 2


def spiral(a, b, theta0, width, colour, direction=1):
    last_x0, last_y0 = xy(a, b, 0, theta0)
    last_x1, last_y1 = xy(a, b, 0, theta0 + width)

    theta = 0
    while a * b ** abs(theta) < 750:
        theta = theta + direction*theta_increment
        x0, y0 = xy(a, b, theta, theta0)
        x1, y1 = xy(a, b, theta, theta0 + width)

        pyxel.tri(last_x0, last_y0, x0, y0, x1, y1, colour)
        pyxel.tri(last_x0, last_y0, last_x1, last_y1, x1, y1, colour)

        last_x0, last_y0 = x0, y0
        last_x1, last_y1 = x1, y1


pyxel.init(1024, 1024)

pyxel.cls(10)
for deg in range(0, 360, 20):
    spiral(2, 1.012, deg, 10, 5)

for deg in range(0, 360, 20):
    spiral(2, 1.012, deg, 10, 2, -1)

for x in range(10,  550, 20):
    r = 1.012 ** x
    for s in range(pyxel.ceil(r/40)):
        pyxel.circb(pyxel.height / 2, pyxel.width / 2, r+s, 7)

pyxel.show()
