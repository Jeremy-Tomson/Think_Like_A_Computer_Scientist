# Q4

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
jeremy = turtle.Turtle()
jeremy.color("blue")
jeremy.pensize(1)


def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)


for i in range(24):
    draw_square(jeremy, 100)
    jeremy.right(15)
wn.mainloop()
