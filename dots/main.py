__all__ = ['draw_large_dots', 'draw_small_dots']
import turtle as t
from random import randint


def draw_large_dots(r, g, b):
    t.hideturtle()
    t.penup()
    t.goto(randint(-400, 400), randint(-300, 300))
    t.pendown()
    t.dot(randint(400, 800), r, g, b)


def draw_small_dots(r, g, b):
    t.hideturtle()
    t.penup()
    t.goto(randint(-400, 400), randint(-300, 300))
    t.pendown()
    t.dot(randint(5, 300), r, g, b)
