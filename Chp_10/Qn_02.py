# Q2

import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
tess.forward(40)
tess.left(90)
tess.forward(50)
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
state_num = 0


def t1():
    tess.forward(70)
    tess.fillcolor("orange")


def t2():
    tess.forward(70)
    tess.fillcolor("red")


def t3():
    tess.back(140)
    tess.fillcolor("green")


timer = 1000

for i in range(timer):
    wn.ontimer(t1, timer)
    wn.ontimer(t2, timer + 1000)
    wn.ontimer(t3, timer + 2000)
    timer += 3000

wn.listen()
wn.mainloop()
