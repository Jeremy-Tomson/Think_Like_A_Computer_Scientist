# Q4

import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tom = turtle.Turtle()
g = turtle.Turtle()
o = turtle.Turtle()
r = turtle.Turtle()
state_num = 0


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


g.penup()
g.forward(40)
g.left(90)
g.forward(50)
g.pendown()
g.shape("circle")
g.shapesize(3)
g.fillcolor("black")

o.penup()
o.forward(40)
g.pendown()
o.left(90)
o.forward(120)
o.shape("circle")
o.shapesize(3)
o.fillcolor("black")

r.penup()
r.forward(40)
g.pendown()
r.left(90)
r.forward(190)
r.shape("circle")
r.shapesize(3)
r.fillcolor("black")


def advance_state_machine():
    global state_num
    if state_num == 0:
        g.fillcolor("green")
        o.fillcolor("black")
        r.fillcolor("black")
        state_num = 1
    elif state_num == 1:
        g.fillcolor("black")
        o.fillcolor("orange")
        r.fillcolor("black")
        state_num = 2
    else:
        g.fillcolor("black")
        o.fillcolor("black")
        r.fillcolor("red")
        state_num = 0


wn.onkey(advance_state_machine, "space")
wn.listen()
wn.mainloop()
