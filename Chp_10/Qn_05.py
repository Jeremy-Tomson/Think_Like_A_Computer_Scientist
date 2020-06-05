# Q5

import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tom = turtle.Turtle()
g = turtle.Turtle()
o = turtle.Turtle()
r = turtle.Turtle()


def draw_housing_2():
    """ Draw a nice housing to hold the traffic lights """
    tom.pensize(3)
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


draw_housing_2()
state_num = 0


g.penup()
g.forward(40)
g.left(90)
g.forward(50)
g.pendown()
g.shape("circle")
g.shapesize(3)
g.fillcolor("green")
g.hideturtle()

o.penup()
o.forward(40)
g.pendown()
o.left(90)
o.forward(120)
o.shape("circle")
o.shapesize(3)
o.fillcolor("orange")
o.hideturtle()

r.penup()
r.forward(40)
g.pendown()
r.left(90)
r.forward(190)
r.shape("circle")
r.shapesize(3)
r.fillcolor("red")
r.hideturtle()


def t1():
    g.showturtle()
    o.hideturtle()
    r.hideturtle()


def t2():
    g.showturtle()
    o.showturtle()
    r.hideturtle()


def t3():
    g.hideturtle()
    o.showturtle()
    r.hideturtle()


def t4():
    g.hideturtle()
    o.hideturtle()
    r.showturtle()


timer = 1000

for i in range(timer):
    wn.ontimer(t1, timer)
    wn.ontimer(t2, timer + 3000)
    wn.ontimer(t3, timer + 4000)
    wn.ontimer(t4, timer + 5000)
    timer += 7000


wn.listen()
wn.mainloop()
