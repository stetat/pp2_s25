randlist = []

while True:
    num = input()
    if num == "":
        break
    else:
        randlist.append(int(num))



def filterp(lprimes):
    newl = []

    for x in lprimes:
        if x >= 1 and all(x % y != 0 for y in range(2, int(x**0.5) + 1)):
            newl.append(x)
    return newl


newlist = filterp(randlist)

for x in newlist:
    print(x)



    