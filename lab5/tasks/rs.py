import re

sr = input("enter some string: ")

x = re.sub("[.]", ":", sr)

print(x)