# Q8

def area_of_circle(r, p):
    a = (r**2) * p
    return a


radius = float(input("What is the radius of the circle?"))
area = area_of_circle(radius, 3.14)
print("The circle with radius,", radius, "has an area of,", area, "units.")
