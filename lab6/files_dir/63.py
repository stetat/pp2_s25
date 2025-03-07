import os

path = "/Users/darhanazibek/Desktop/pp2_s25"

if os.path.exists(path):
    print(os.path.dirname(path), "\n", os.path.basename(path))

else:
    print("The path does not exist")