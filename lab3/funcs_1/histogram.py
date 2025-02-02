my_list = []

while True:
    num = input("enter a number: ")
    if num == "":
        break
    else:
        my_list.append(int(num))


def histogram(some):
    for x in some:
        print("*"*x)

histogram(my_list)