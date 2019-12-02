# Q11

import math


def is_rightangled(s1, s2, s3):
    if abs((math.sqrt(s1**2 + s2**2)) - s3) < 0.00001:
        print("True")
    else:
        print("False")


is_rightangled()
