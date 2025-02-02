mainl = []

while True:
    x = input()
    if x == "":
        break
    else:
        mainl.append(int(x))


def to3(slist):
    for i in range(len(slist)-2):
        if slist[i] == 0 and slist[i+1] == 0 and slist[i+2] == 7:
                return True
                

    return False

print(to3(mainl))