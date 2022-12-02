__all__ = ['color_test', 'write_lightness', 'new_line', 'draw_line']

import turtle as t
from .random_rgb import *


def color_test():
    t.hideturtle()
    t.penup()
    t.goto(-300, 250)
    write_title()

    t.pendown()
    t.pensize(10)
    t.colormode(255)

    lightness = 727   # от 3 до 765, 38 – это 5%
    line_no = 1

    while lightness < 3 or lightness > 765 or line_no < 20:  # количество рядов
        for color_no in range(10):  # количество элементов в ряду
            print('color_no -', color_no)
            draw_square(*random_rgb(lightness))

        write_lightness(lightness)
        new_line()
        line_no += 1
        print('line_no -', line_no)
        lightness -= 38  # 38 – это 5%

    t.done()


# Turtle draws stripes
def draw_line(rgb_r1, rgb_g1, rgb_b1):
    t.pencolor(rgb_r1, rgb_g1, rgb_b1)
    t.goto(t.xcor() + 20, t.ycor())


# Turtle draws squares
def draw_square(rgb_r1, rgb_g1, rgb_b1):
    if rgb_r1 < 1 or rgb_g1 < 1 or rgb_b1 < 1 or rgb_r1 > 765 or rgb_g1 > 765 or rgb_b1 > 765:
        print('Error', rgb_r1, rgb_g1, rgb_b1)
        return
    t.speed(10)
    t.pensize(0)
    t.pendown()
    t.color(rgb_r1, rgb_g1, rgb_b1)
    t.pencolor(1, 1, 1)
    t.begin_fill()
    for side_no in range(4):
        t.forward(20)
        t.left(-90)
    t.end_fill()
    t.penup()
    t.goto(t.xcor() + 20, t.ycor())


def new_line():
    t.penup()
    t.goto(-300, t.ycor()-20)
    t.pendown()


def write_lightness(lightness1):
    t.penup()
    t.goto(t.xcor() + 10, t.ycor() - 17)
    t.pencolor(1, 1, 1)
    t.write(f'{int((lightness1/765)*100)}% (R+G+B={lightness1})', move=False, align='left', font=('Arial', 14, 'normal'))
    t.goto(t.xcor(), t.ycor() + 17)
    t.pendown()


def write_title():
    t.pendown()
    t.pencolor('black')
    start_x = t.xcor()
    t.write('Random RGB colors', move=False, align='left', font=('Arial', 26, 'normal'))
    t.penup()
    t.goto(start_x, t.ycor() - 20)
