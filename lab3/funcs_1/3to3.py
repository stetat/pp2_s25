mainl = []

while True:
    x = input()
    if x == "":
        break
    else:
        mainl.append(int(x))


def to3(slist):
    for i in range(len(slist)):
        if i+1 < len(slist) and slist[i] == 3 and slist[i+1] == 3:
            return True
            

    return False

print(to3(mainl))