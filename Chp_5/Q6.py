# Q6

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]


def grade(s):
    if s >= 75:
        print("A")
    elif 70 <= s < 75:
        print("B")
    elif 60 <= s < 70:
        print("C")
    elif 50 <= s < 60:
        print("D")
    elif 45 <= s < 50:
        print("E")
    elif 40 <= s < 45:
        print("F")
    elif s < 40:
        print("U")


for i in xs:
    grade(i)
