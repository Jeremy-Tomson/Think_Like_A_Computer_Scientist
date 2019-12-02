# Q6

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
jeremy = turtle.Turtle()
jeremy.color("hotpink")
jeremy.pensize(3)


def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


def draw_equilateral_triangle(t, sz):
    draw_poly(t, 3, sz)


draw_equilateral_triangle(jeremy, 100)

wn.mainloop()
