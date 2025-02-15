def squares(a, b):
    
    while a <= b:
        yield a**2
        a+=1

a = int(input("Enter the lower bound : "))
b = int(input("Enter the upper bound : "))

ex = squares(a, b)

for x in ex:
    print(x, end=" ")