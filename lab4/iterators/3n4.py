def d34(n):
    x = 0

    while x < n:
        if x%3 == 0 and x%4 == 0:
            yield x
        x+=1

n = int(input("Enter the limit: "))

test = d34(n)

for x in test:
    print(x, end=" ")