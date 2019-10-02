# Q8

import turtle


def draw_bar(t, height):
    if height >= 200:
        tess.color("blue", "red")
    if 100 <= height < 200:
        tess.color("blue", "yellow")
    if height < 100:
        tess.color("blue", "green")

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()


wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()
