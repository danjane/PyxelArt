import pyxel

pyxel.init(512, 512)

def wave(height, colour):
    for x in range(512):
        y = height + 10*pyxel.sin(height*3 + x*2)
        pyxel.line(x, y, x+5, y-5, colour)

def wave_set(min, max, colour):
    for height in range(min, max, 10):
        wave(height, colour)

pyxel.cls(0)

wave_set(0, 150, 8)
wave_set(140, 240, 4)
wave_set(240, 310, 10)
wave_set(310, 350, 6)
wave_set(350, 512, 7)

pyxel.show()