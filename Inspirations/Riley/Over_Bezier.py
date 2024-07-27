import pyxel
import numpy as np

def bezier_point(t, points):
    """ Calculate the position of a point on the Bezier curve at parameter t """
    n = len(points) - 1
    x, y = 0, 0
    # Calculate point on the Bezier curve using the Bernstein polynomial
    for i, (px, py) in enumerate(points):
        binomial_coeff = np.math.comb(n, i)
        term = binomial_coeff * ((1 - t) ** (n - i)) * (t ** i)
        x += term * px
        y += term * py
    return x, y

def draw_bezier_curve(points, segments=100):
    """ Draw a Bezier curve based on given control points """
    pyxel.cls(0)
    for i in range(segments):
        t1 = i / segments
        t2 = (i + 1) / segments
        x1, y1 = bezier_point(t1, points)
        x2, y2 = bezier_point(t2, points)
        pyxel.line(x1, y1, x2, y2, 7)

def update():
    pass

def main():
    control_points = [(10, 100), (60, 10), (110, 200), (160, 100)]
    pyxel.init(180, 180, caption="Bezier Curve Example")
    pyxel.run(update, lambda: draw_bezier_curve(control_points))

main()
