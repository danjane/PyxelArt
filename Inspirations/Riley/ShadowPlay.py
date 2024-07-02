import pyxel

rectangle_size = [80, 40]
rectangle_count = [8, 30]

shear_factor = 0.6

pyxel.init(rectangle_size[0]*rectangle_count[0], rectangle_size[1]*rectangle_count[1])

# Define the custom colors as hex strings
custom_colors_hex = [
    0x1E3A5F,  # Dark Blue
    0x5AC8FA,  # Light Blue
    0x17A589,  # Turquoise
    0xF48FB1,  # Pink
    0xFFC1E3,  # Light Pink
    0x9B59B6,  # Purple
    0xD7BDE2,  # Light Purple
    0xF39C12,  # Orange
    0xF4D03F,  # Yellow
    0x27AE60,  # Dark Green
    0x82E0AA,  # Light Green
    0xE74C3C,  # Red
    0xF5B7B1,  # Peach
    0x7F8C8D   # Grey
]

# Use the colors.from_list method to create a custom palette
pyxel.colors.from_list(custom_colors_hex)

# Draw the rectangles with random colours
for i in range(0, pyxel.width, rectangle_size[0]):
    for j in range(0, pyxel.height + pyxel.ceil(shear_factor*pyxel.width), rectangle_size[1]):
        pyxel.rect(i, j, rectangle_size[0], rectangle_size[1], pyxel.rndi(0, len(custom_colors_hex)))

# Apply a skew
for x in range(pyxel.width):
    for y in range(pyxel.height + pyxel.ceil(shear_factor*pyxel.width)):
        color = pyxel.pget(x, y)
        # Calculate new_x by adding a shift that increases with y coordinate
        new_y = y - int(x * shear_factor)
        pyxel.pset(x, new_y, color)

pyxel.show()