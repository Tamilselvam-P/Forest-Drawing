import turtle
import random

# Global variables to store turtle's state
saved_position = (0, 0)
saved_pen_color = ""
saved_fill_color = ""

def draw_triangle(centre_x, centre_y, width, height, pen_color, fill_color):
    save_state()
    turtle.penup()
    turtle.goto(centre_x, centre_y)
    turtle.pendown()
    turtle.color(pen_color, fill_color)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(width / 2)
    turtle.left(120)
    turtle.forward(width)
    turtle.left(120)
    turtle.forward(width)
    turtle.left(120)
    turtle.forward(width / 2)
    turtle.end_fill()
    restore_state()

def draw_rectangle(centre_x, centre_y, width, height, pen_color, fill_color):
    save_state()
    turtle.penup()
    turtle.goto(centre_x - width / 2, centre_y - height / 2)
    turtle.pendown()
    turtle.color(pen_color, fill_color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()
    restore_state()

def draw_circle(centre_x, centre_y, radius, pen_color, fill_color):
    save_state()
    turtle.penup()
    turtle.goto(centre_x, centre_y - radius)
    turtle.pendown()
    turtle.color(pen_color, fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    restore_state()

def stamp_turtle(centre_x, centre_y, color):
    save_state()
    turtle.penup()
    turtle.goto(centre_x, centre_y)
    turtle.pendown()
    turtle.color(color)
    turtle.stamp()
    restore_state()

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def save_state():
    global saved_position, saved_pen_color, saved_fill_color
    saved_position = turtle.position()
    saved_pen_color = turtle.pencolor()
    saved_fill_color = turtle.fillcolor()

def restore_state():
    turtle.penup()
    turtle.goto(saved_position)
    turtle.pendown()
    turtle.pencolor(saved_pen_color)
    turtle.fillcolor(saved_fill_color)