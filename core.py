__all__ = ['main_action']
import turtle as t
from random import randint

from colors import *
from dots import *
from initial_data import *
from lines import *
from symbols import *


def main_action(text):
    global pen_size, type_size
    t.colormode(255)
    dots_amount = randint(1, 5)
    for dot_no in range(dots_amount):
        draw_large_dots(*random_rgb(700))

    dots_amount = randint(5, 10)
    for dot_no in range(dots_amount):
        draw_small_dots(*random_rgb(550))

    new_line(*random_rgb(250))
    t.goto(start_x, start_y)
    t.pensize(pen_size)

    for word in text.split():  # перебираем строки
        for current_symbol in list(word):  # перебираем символы
            if current_symbol in how_to_draw_all_symbols:
                type_symbol(current_symbol, type_size, pen_size * 1.5)

        if type_size > 2:
            type_size *= 0.8
        if pen_size > 1:
            pen_size *= 0.8

        t.goto(start_x, t.ycor() - ((4 + line_space) * type_size * 5))  # идём в точку начала новой строки
        t.pensize(pen_size)
        new_line(*random_rgb(250))

    t.done()
