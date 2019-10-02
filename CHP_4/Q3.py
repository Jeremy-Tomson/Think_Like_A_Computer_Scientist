# Q3

import turtle


def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


wn = turtle.Screen()
wn.bgcolor("lightgreen")

jeremy = turtle.Turtle()
jeremy.color("hotpink")
jeremy.pensize(3)
draw_poly(jeremy, 8, 50)

wn.mainloop()
