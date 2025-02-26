import re

sr = input("enter some string: ")

x = re.sub("(?<=[a-z])(?=[A-Z])", " ", sr)

print(x)