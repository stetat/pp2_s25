import re

sr = input("enter some string: ")

x = re.split("[A-Z]", sr)

print(x)