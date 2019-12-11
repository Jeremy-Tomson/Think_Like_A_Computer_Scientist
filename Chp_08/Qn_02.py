# Q2

prefixes = "JKLMNOPQ"
suffix = "ack"
suffix_1 = "uack"

for p in prefixes:
    if p == "O" or p == "Q":
        print(p + suffix_1)
    else:
        print(p + suffix)
