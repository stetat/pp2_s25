li = []

while True:
    num = input("Enter a number: ")
    if num == "":
        break
    else:
        li.append(int(num))

def unique(some):
    log = []
    ulist = []
    for x in some:
        if x in log:
            continue
        else:
            ulist.append(x)
            log.append(x)

    return ulist

liun = unique(li)


print("List of unique elements: ")
for x in liun:
    print(x)