import os

f = open("1.txt", "r")
g = open("2.txt", "a")

g.writelines(f)