def sqrs(n):
    x = 1
    while x <= n:
        yield x**2
        x+=1

n = int(input("Enter the limit: "))

ex = sqrs(n)

for x in ex:
    print(x, end=" ")