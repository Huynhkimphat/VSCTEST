# for loop
import turtle
qazi_turtle = turtle.Turtle()


def square():
    qazi_turtle.forward(100)
    qazi_turtle.right(60)
    qazi_turtle.forward(100)
    qazi_turtle.right(60)
    qazi_turtle.forward(100)
    qazi_turtle.right(60)
    qazi_turtle.forward(100)


for i in range(10):
    square()
