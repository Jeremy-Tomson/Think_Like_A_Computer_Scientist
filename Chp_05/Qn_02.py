# Q2

start = int(input("What is the starting day?"))
if start < 0 or start > 6:
    print("Error")
    exit()

length = int(input("How long do you plan on staying?"))
if length < 0:
    print("Error")
    exit()

total = length - start
days = total % 7
weeks = ((total-days)/7)

print()

if days == 0:
    print("Your stay wil end in", int(weeks), "weeks, and", days, "day(s). Which is a Sunday.")
elif days == 1:
    print("Your stay wil end in", int(weeks), "weeks, and", days, "day(s). Which is a Monday.")
elif days == 2:
    print("Your stay wil end in", int(weeks), "weeks, and", days, "day(s). Which is a Tuesday.")
elif days == 3:
    print("Your stay wil end in", int(weeks), "weeks, and", days, "day(s). Which is a Wednesday.")
elif days == 4:
    print("Your stay wil end in", int(weeks), "weeks, and", days, "day(s). Which is a Thursday.")
elif days == 5:
    print("Your stay wil end in", int(weeks), "weeks, and", days, "day(s). Which is a Friday.")
elif days == 6:
    print("Your stay wil end in", int(weeks), "weeks, and", days, "day(s). Which is a Saturday.")
else:
    print("Error")
