import math

r = int(input("Enter the radius of the sphere: "))

def vol(x):
    return round((4/3) * math.pi * r**3, 3)

print(vol(r))