import pyxel

edges = [0]
s = 0
w = 11
while s < 100:
    s = s + abs(w)
    edges.append(s)
    w = w - 1

pyxel.init(edges[-1], 100)

for i in range(len(edges)):
    for j in range(8):
        pyxel.rect(edges[i], 10*j, 11, 11, ((i + j) % 2)*7)

pyxel.show()

