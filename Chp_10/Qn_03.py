# Q3

import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tom = turtle.Turtle()
g = turtle.Turtle()
o = turtle.Turtle()
r = turtle.Turtle()


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


def draw_housing_2():
    """ Draw a nice housing to hold the traffic lights """
    tom.pensize(3)
    tom.penup()
    tom.forward(200)
    tom.pendown()
    tom.color("black", "darkgrey")
    tom.begin_fill()
    tom.forward(80)
    tom.left(90)
    tom.forward(200)
    tom.circle(40, 180)
    tom.forward(200)
    tom.left(90)
    tom.end_fill()
    tom.hideturtle()


draw_housing()
draw_housing_2()

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

g.penup()
g.forward(240)
g.left(90)
g.forward(50)
g.pendown()
g.shape("circle")
g.shapesize(3)
g.fillcolor("green")
g.hideturtle()

o.penup()
o.forward(240)
g.pendown()
o.left(90)
o.forward(120)
o.shape("circle")
o.shapesize(3)
o.fillcolor("orange")
o.hideturtle()

r.penup()
r.forward(240)
g.pendown()
r.left(90)
r.forward(190)
r.shape("circle")
r.shapesize(3)
r.fillcolor("red")
r.hideturtle()


def advance_state_machine():
    global state_num
    if state_num == 0:
        g.showturtle()
        o.hideturtle()
        r.hideturtle()
        state_num = 1
    elif state_num == 1:
        g.hideturtle()
        o.showturtle()
        r.hideturtle()
        state_num = 2
    else:
        g.hideturtle()
        o.hideturtle()
        r.showturtle()
        state_num = 0


wn.onkey(advance_state_machine, "space")
wn.listen()
wn.mainloop()

# Most modern day traffic lights involve the use of a timer to dictate whether a traffic light goes on or off.
# When a certain light needs to be displayed the other lights go off.
