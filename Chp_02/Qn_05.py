# Q5

p = 10000
n = 100
r = 8

t = int(input("How many years will your amount be compounded for?"))

a = (p * ((1 + (r/n)) ** t))

print("You will have", int(a), "after", t, "years.")
