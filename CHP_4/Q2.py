# Q2

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


size = 20
for i in range(5):
    draw_square(jeremy, size)
    size = size + 20
    jeremy.penup()
    jeremy.right(135)
    jeremy.forward(14)
    jeremy.right(-135)
    jeremy.pendown()

wn.mainloop()
