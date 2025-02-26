import re

sr = input("enter some string: ")

pattern = r"[a-z]+_[a-z]+"

case = re.findall(pattern, sr)

for x in case:
    print(x)