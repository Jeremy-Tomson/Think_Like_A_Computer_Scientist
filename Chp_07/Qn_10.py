# Q10


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            print("False")
        else:
            print("True for:", i)


is_prime(11)
