# Q3


def count_letters(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count


print(count_letters("banana", "a"))
