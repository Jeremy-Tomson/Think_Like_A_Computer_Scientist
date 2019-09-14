# Q9
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
jeremy = turtle.Turtle()
jeremy.color("hotpink")
jeremy.pensize(3)


def draw_star(t, sz):
    for i in range(5):
        t.forward(sz)
        t.right(144)
    t.penup()
    t.forward(sz * 2)
    t.pendown()


draw_star(jeremy, 100)

wn.mainloop()
