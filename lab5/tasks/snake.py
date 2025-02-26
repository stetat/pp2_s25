import re

sr = input("enter some string: ")

x = re.sub("([A-Z])", lambda match: "_"+match.group(1).lower(), sr)

print(x)