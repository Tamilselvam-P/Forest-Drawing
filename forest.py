import turtle
import random
import utilities
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
DRAWING_RECT_WIDTH = 700
DRAWING_RECT_HEIGHT = 700
TREE_SELECTOR_RADIUS = 10
TREE_SELECTOR_CENTER_1 = (0, 370)
TREE_SELECTOR_CENTER_2 = (100, 370)
BIRD_LOCATION = (-340, 370)
STEM_WIDTH = 15
STEM_HEIGHT = 80
LEAVES_WIDTH = 100
LEAVES_HEIGHT = 50
LEAVES_OVERLAP = 0.4
current_drawing_mode = "tree"
current_tilt_angle = 0
def handle_click(x, y):
    global current_drawing_mode
    if is_point_inside_circle(x, y, TREE_SELECTOR_CENTER_1, TREE_SELECTOR_RADIUS):
        current_drawing_mode = "tree"
    elif is_point_inside_circle(x, y, TREE_SELECTOR_CENTER_2, TREE_SELECTOR_RADIUS):
        current_drawing_mode = "bird"
    else:
        if is_point_inside_rectangle(x, y):
            if current_drawing_mode == "tree":
                draw_tree(x, y)
            elif current_drawing_mode == "bird":
                draw_bird(x, y)
def is_point_inside_circle(x, y, center, radius):
    distance_squared = (x - center[0]) ** 2 + (y - center[1]) ** 2
    return distance_squared <= radius ** 2
def is_point_inside_rectangle(x, y):
    half_width = DRAWING_RECT_WIDTH / 2
    half_height = DRAWING_RECT_HEIGHT / 2
    return -half_width <= x <= half_width and -half_height <= y <= half_height
def draw_tree(x, y):
    stem_scale = random.uniform(0.7, 1.3)
    leaves_scale = random.uniform(0.7, 1.3)
    stem_height = STEM_HEIGHT * stem_scale
    leaves_height = LEAVES_HEIGHT * leaves_scale
    leaves_width = LEAVES_WIDTH * leaves_scale
    stem_y = y - stem_height / 2
    utilities.draw_rectangle(x, stem_y, STEM_WIDTH, stem_height, "brown", "brown")
    left_leaf_x = x - leaves_width / 2
    right_leaf_x = x + leaves_width / 2
    leaves_y = stem_y + stem_height * LEAVES_OVERLAP
    utilities.draw_triangle(x, leaves_y, leaves_width, leaves_height, "green", "green")
    utilities.draw_triangle(left_leaf_x, leaves_y, leaves_width, leaves_height, "green", "green")
    utilities.draw_triangle(right_leaf_x, leaves_y, leaves_width, leaves_height, "green", "green")
def draw_bird(x, y):
    turtle.tiltangle(current_tilt_angle)
    utilities.stamp_turtle(x, y, "black")
def handle_left_keypress():
    global current_tilt_angle
    current_tilt_angle += 10
def handle_right_keypress():
    global current_tilt_angle
    current_tilt_angle -= 10
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
turtle.speed(0)
turtle.hideturtle()
turtle.register_shape('bird', ((-22, -39), (-20, -7), (-7, 3), (-11, 7), (-12, 9), (-11, 10), (-9, 10), (-3, 7),(10, 24), (30, 16), (13, 18), (4, 0), (14, -6), (6, -13), (0, -4), (-14, -13),(-22, -39)))
turtle.shape('bird')
utilities.draw_rectangle(0, 0, DRAWING_RECT_WIDTH, DRAWING_RECT_HEIGHT, "black", "")
utilities.draw_circle(TREE_SELECTOR_CENTER_1[0], TREE_SELECTOR_CENTER_1[1], TREE_SELECTOR_RADIUS, "black", "")
utilities.draw_circle(TREE_SELECTOR_CENTER_2[0], TREE_SELECTOR_CENTER_2[1], TREE_SELECTOR_RADIUS, "black", "")
turtle.penup()
turtle.goto(TREE_SELECTOR_CENTER_1[0] - 15, TREE_SELECTOR_CENTER_1[1] - 20)
turtle.write("Tree", align="center", font=("Arial", 12, "normal"))
turtle.goto(TREE_SELECTOR_CENTER_2[0] - 15, TREE_SELECTOR_CENTER_2[1] - 20)
turtle.write("Bird", align="center", font=("Arial", 12, "normal"))
turtle.onscreenclick(handle_click)
turtle.onkey(handle_left_keypress, "Left")
turtle.onkey(handle_right_keypress, "Right")
turtle.listen()
turtle.done()