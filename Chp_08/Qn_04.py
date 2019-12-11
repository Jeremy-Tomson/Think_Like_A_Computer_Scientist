# Q4


def count_letters(string, ch, start):
    ss = string
    c = ch
    s = start
    e = len(string)
    if s < len(string):
        for i in range(s, e):
            if string[i] == ch:
                print(ss.find(c, i))


print(count_letters("banana banana banana", "a", 0))
