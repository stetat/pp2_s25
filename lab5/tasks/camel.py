import re

sr = input("enter some string: ")

x = re.sub("_([a-z])", lambda match: match.group(1).upper(), sr)

print(x)