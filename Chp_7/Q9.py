# Q9


def print_triangular_numbers(n):
    for i in range(n + 1):
        t = (i*(i + 1))/2
        print(i, "\t", int(t))


print_triangular_numbers(5)
