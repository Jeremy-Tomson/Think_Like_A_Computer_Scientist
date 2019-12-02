# Q5


def sum_up(xs):
    sum = 0
    for x in xs:
        if x % 2 == 1:
            sum += x
        if x % 2 == 0:
            break
    print(sum)


sum_up([1, 3, 7, 14, 15, 6, 8, 9, 12])

