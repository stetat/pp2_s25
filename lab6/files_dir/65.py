f = open('t.txt', 'a')

ulist = []

while True:
    n = input("enter a num: ")
    ulist.append(n)

    if n == '':
        break


f.writelines(ulist)