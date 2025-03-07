import math

a = []

while True:
    n = input("enter a num: ")

    if n == '':
        break

    a.append(int(n))

print(math.prod(a))