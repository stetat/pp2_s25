import os

od = []
of = []

path = '/Users/darhanazibek/Desktop/pp2_s25'

for x in os.listdir(path):
    if os.path.isdir(f'{path}/{x}'):
        od.append(x)

print(od, "\n")

for x in os.listdir(path):
    if not (os.path.isdir(f'{path}/{x}')):
        of.append(x)

print(of, "\n")


print(os.listdir('/Users/darhanazibek/Desktop/pp2_s25/'), "\n")

