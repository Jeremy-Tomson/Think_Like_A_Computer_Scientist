# Q10
# a)
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


for i in range(5):
    draw_star(jeremy, 100)
    jeremy.penup()
    jeremy.forward(350)
    jeremy.right(144)
    jeremy.pendown()

wn.mainloop()

# b)
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


for i in range(5):
    draw_star(jeremy, 100)
    jeremy.forward(350)
    jeremy.right(144)

wn.mainloop()
