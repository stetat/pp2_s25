a = str(input("Enter a phrase/word: "))

def pali(x):
    
    return x == x[::-1]

print(pali(a))
