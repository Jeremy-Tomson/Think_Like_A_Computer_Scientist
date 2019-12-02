# Q12

import math


def is_rightangled(a, b, c):

    if a > b and c:
        s1 = c
        s2 = b
        s3 = a
    elif b > c and a:
        s1 = c
        s2 = a
        s3 = b
    elif c > a and b:
        s1 = b
        s2 = a
        s3 = c
    if abs((math.sqrt(s1**2 + s2**2)) - s3) < 0.00001:
        print("True")
    else:
        print("False")


is_rightangled()
