__all__ = ['type_symbol']
import turtle as t
from . symbols import *
from . move_cursor import move


def type_symbol(symbol, size, pen_size):
    for line in how_to_draw_all_symbols[symbol]:
        x, y, *pen = line
        pen = int(*pen)

        if pen == 1:
            t.penup()
            move(x, y, size)
        elif pen == 2:
            t.dot(pen_size)
        else:
            t.pendown()
            move(x, y, size)

    t.penup()
    move(1, 0, size)
