# Q1

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
jeremy = turtle.Turtle()
jeremy.color("hotpink")
jeremy.pensize(3)


def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.forward(sz * 2)
    t.pendown()


draw_square(jeremy, 30)
draw_square(jeremy, 30)
draw_square(jeremy, 30)
draw_square(jeremy, 30)
draw_square(jeremy, 30)

wn.mainloop()
