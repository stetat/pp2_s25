a = str(input("Enter any string: "))

uc = 0
lc = 0

for x in a:
    if x.isupper():
        uc+=1
    else:
        lc+=1

print(f"there are {uc} uppercase letters\nand {lc} lowercase letters")