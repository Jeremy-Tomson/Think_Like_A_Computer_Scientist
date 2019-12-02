# Q6


def sum_sam(xs):
    count = 0
    for x in xs:
        if x != "Sam":
            count += 1
        elif x == "Sam":
            count += 1
            break
    print(count)


sum_sam(["Jack", "Tom", "Allan", "Grant", "Jeff", "James", "Sam", "John"])

