import pyxel

W = 500
N = 40

pyxel.init(W, W)
pyxel.colors[0] = 0x555555
pyxel.colors[1] = 0xcccccc


def plot_contour_lines(height):
    for x in range(W):
        for y in range(W):
            colour = pyxel.floor(height[x][y]) % 2
            pyxel.pset(x, y, colour)


def height_vertical_lines():
    height = []
    for x in range(W):
        height.append([2 * N * x / W] * W)
    return height


def up(cx, cy, height):
    for x in range(W):
        for y in range(W):
            r = ((cx - x) ** 2 + (cy - y) ** 2) ** 0.5
            height[x][y] = height[x][y] + 1/(1+(r/20)**2)
    return height


h = height_vertical_lines()

def update():
    global h
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        h = up(pyxel.mouse_x, pyxel.mouse_y, h)

def draw():
    plot_contour_lines(h)

pyxel.run(update, draw)
