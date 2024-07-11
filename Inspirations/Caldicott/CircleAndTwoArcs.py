# https://www.artsper.com/us/contemporary-artworks/drawing/521852/untitled-2014-id-388

import pyxel


def draw_arc(cx, cy, theta0, theta1):

    # Determine the number of segments
    segments = 20  # You can adjust this for smoother arcs

    # Calculate the angle step per segment
    angle_step = (theta1 - theta0) / segments

    # Draw each segment
    for i in range(segments):
        # Start point of the segment
        x0 = cx + r * pyxel.cos(theta0 + i * angle_step)
        y0 = cy + r * pyxel.sin(theta0 + i * angle_step)

        # End point of the segment
        x1 = cx + r * pyxel.cos(theta0 + (i + 1) * angle_step)
        y1 = cy + r * pyxel.sin(theta0 + (i + 1) * angle_step)

        # Draw the line segment
        pyxel.line(x0, y0, x1, y1, 1)



phi = (1 + 5**0.5)/2

pyxel.init(726, 1024)

pyxel.colors[0] = 0xAFD6B4
pyxel.cls(0)

pyxel.colors[1] = 0x240851
w = pyxel.width / phi
pyxel.line(w, 0, w, pyxel.height, 1)

r = w / 4
pyxel.circb(w-r, 3*r, r, 1)


def draw_left_arc_on_line(angle, vy):
    draw_arc(w + r*pyxel.cos(angle), vy, 180-angle, 180+angle)

def draw_right_arc_on_line(angle, vy):
    draw_arc(w - r*pyxel.cos(angle), vy, -angle, angle)

draw_left_arc_on_line(60, 4*r-30)
draw_right_arc_on_line(120, 5*r-30)

pyxel.circ(w+r/6, 3*r-15, r/6, 1)
pyxel.circ(w-r/6, 6*r-45, r/6, 1)

pyxel.show()
