a = str(input("Enter any string: "))


if a == "".join(reversed(a)):
    print("The string is a palindrome!")
else:
    print("The string isnt a palindrome")