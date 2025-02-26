
from prettytable import PrettyTable
import re

f = open("row.txt", "r")
work = f.read()

table = PrettyTable(['id', 'name'])

pattern = r"[1-9]+.\s(?P<ItemName>.*)\s[1-9],000"

comp = re.compile(pattern)
look = comp.finditer(work)

do = re.finditer(pattern, work)

c = 1
for x in do:
    table.add_row([f'{c}', f'{x.group("ItemName")}'])
    c+=1


print(table)
    

