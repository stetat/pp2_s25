def down(n):
    x = 0
    while(n >= 0):
        yield n
        n-=1

n = int(input("Enter the starter: "))
test = down(n)

for x in test:
    print(x, end=" ")