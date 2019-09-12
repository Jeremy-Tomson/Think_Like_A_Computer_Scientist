# Q12

import turtle
wn = turtle.Screen()
jeremy = turtle.Turtle()
wn.bgcolor("lightgreen")
jeremy.shape("turtle")
jeremy.color("blue")
jeremy.stamp()
jeremy.pensize(5)

for i in range(12):
    jeremy.penup()
    jeremy.forward(100)
    jeremy.pendown()
    jeremy.forward(20)
    jeremy.penup()
    jeremy.forward(20)
    jeremy.stamp()
    jeremy.forward(-140)
    jeremy.right(30)

wn.mainloop()
