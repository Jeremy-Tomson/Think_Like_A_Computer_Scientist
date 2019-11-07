# Q8

z = 0
z = 0
y = 0

while z == 0:
    t = int(input("What time is it? (12 hour format)"))
    if t > 12:
        print("Error!")
    else:
        z = z + 1

print("Your selected start time is", t, "o'clock")


tw = int(input("How long do you want to set the alarm for?"))
nt = tw % 24

if nt > 12:
   nt = nt - 12
   print("Your alarm will go off at", nt, "o'clock")

elif nt < 12:
   print("Your alarm will go off at", nt, "o'clock")
