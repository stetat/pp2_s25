far = int(input("Enter farenheit tempretature: "))

def ctof(f):
    return (5 / 9) * (f-32)

print(f"{far} farenheits is {round(ctof(far), 4)} in celcius")