import datetime

y, m, d = int(input("Enter year 1: ")), int(input("Enter month 1: ")), int(input("Enter day 1: "))
y1, m1, d1 = int(input("Enter year 2: ")), int(input("Enter month 2: ")), int(input("Enter day 2: "))

dif = datetime.datetime(y1, m1, d1) - datetime.datetime(y, m, d)

print(dif)