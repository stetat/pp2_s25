import re

sr = input("Enter a string: ")


pattern = r"ab*"

case = re.finditer(pattern, sr)

for x in case:
    print(x.group())