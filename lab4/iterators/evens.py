def ev(n):
    x = 0

    while x < n:
        if x % 2 == 0:
            yield x

        x+=1

n = int(input("Enter the limit: "))

ex = ev(n)
ex_list = list(ex)

for i, x in enumerate(ex_list):
    if i != len(ex_list) - 1:  
        print(x, end=", ")
    else:
        print(x)  
