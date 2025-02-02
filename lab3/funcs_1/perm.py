a = str(input("Input a string: "))

def perm(string, base=""):
    if string == "":
        print(f"{base}\n")
    for i in range(len(string)):
        remaining = string[:i] + string[i+1:]
        
        perm(remaining, base + string[i])


perm(a)

            
        