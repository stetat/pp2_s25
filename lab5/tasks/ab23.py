import re

sr = input("Enter a string: ")


pattern = r".*ab{2,3}\b"

case = re.findall(pattern, sr)

for x in case:
    print(x)