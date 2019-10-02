# Q5
# a)

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
jeremy = turtle.Turtle()
jeremy.color("blue")
jeremy.pensize(1)


def draw_multicolor_square(t, sz):
    t.forward(sz)
    t.left(90)


size = 1
for i in range(100):
    draw_multicolor_square(jeremy, size)
    size = size + 2

wn.mainloop()

# b)

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
jeremy = turtle.Turtle()
jeremy.color("blue")
jeremy.pensize(1)


def draw_multicolor_square(t, sz):
    t.forward(sz)
    t.left(90)


size = 1
for i in range(100):
    draw_multicolor_square(jeremy, size)
    size = size + 2
    jeremy.left(1)

wn.mainloop()
