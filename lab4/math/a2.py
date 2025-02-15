import math

ns = int(input("Input number of sides: "))
ls = int(input("Input the length of a side: "))
apth = (ls)/(2*(math.tan(math.radians(180/ns))))

print(f"The area of the polygon is: {round((ns*ls*apth)/2, 2)}")