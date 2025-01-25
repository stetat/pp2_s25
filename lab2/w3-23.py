#lists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


print(thislist[:-2])


thislist[1] = 123
print(thislist)


thislist.append("orange")
print(thislist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


fruits.sort(reverse=True)
print(fruits)