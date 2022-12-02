import turtle


# Turtle module motion control
def move(x, y, size):
    turtle.goto(turtle.xcor() + (x * size * 5), turtle.ycor() + (y * size * 5))
