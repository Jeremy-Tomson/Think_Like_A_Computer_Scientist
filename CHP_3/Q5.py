# Q5
# a)

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    print(i)

# b)

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    print(i, i ** 2)

# c)

total = 0

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    total = sum(xs)
print(total)

# d)

import numpy
total = 0

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    total = numpy.prod(xs)
print(total)
