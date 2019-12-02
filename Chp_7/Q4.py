# Q4


def len_five(xs):
    count = 0
    for x in xs:
        if len(x) == 5:
            count += 1
    print(count)


len_five(["Hello", "Goodbye", "Present", "Dirty", "Happy", "Apple"])

