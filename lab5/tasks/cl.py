import re

sr = input("enter some string: ")

pattern = r"[A-Z]{1}[a-z]+"

case = re.findall(pattern, sr)

for x in case:
    print(x)