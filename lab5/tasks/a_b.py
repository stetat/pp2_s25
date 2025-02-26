import re

sr = input("enter some string: ")

pattern = r"a.*b"

case = re.findall(pattern, sr)

for x in case:
    print(x)