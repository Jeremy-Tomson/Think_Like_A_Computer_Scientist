# Q12

import turtle
wn = turtle.Screen()
dp = turtle.Turtle()


def drunk_pirates(a, d):
    dp.left(a)
    dp.forward(d)


drunk_pirates(90, 100)
drunk_pirates(90, 100)
drunk_pirates(-135, 71.15)
drunk_pirates(-90, 71.15)
drunk_pirates(-90, 141.42)
drunk_pirates(135, 100)
drunk_pirates(135, 141.42)
drunk_pirates(135, 100)

wn.mainloop()
