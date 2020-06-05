# Q1

import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.pensize(3)
size_up = 0
size_down = 0


def h1():
    tess.forward(30)


def h2():
    tess.left(45)


def h3():
    tess.right(45)


def h4():
    tess.color("red")


def h5():
    tess.color("green")


def h6():
    tess.color("blue")


def h7():
    tess.pensize(5)


def h8():
    tess.pensize(1)


def h9():
    tess.pensize(3)


def h10():
    tess.forward(45)


def h11():
    tess.forward(15)


def h12():
    wn.bye()


wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "r")
wn.onkey(h5, "g")
wn.onkey(h6, "b")
wn.onkey(h7, "=")
wn.onkey(h8, "-")
wn.onkey(h9, "0")
wn.onkey(h10, "w")
wn.onkey(h11, "i")
wn.onkey(h12, "q")

wn.listen()
wn.mainloop()
print(size_up)
