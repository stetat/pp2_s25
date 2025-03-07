import os

count = 0

fil = open("t.txt", "r")


for i in fil:
    count+=1

print(count)