# Q7


def sqrt(n):
    approx = n/2.0
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        approx = better
        print("\t", better)


print(sqrt(25.0))

