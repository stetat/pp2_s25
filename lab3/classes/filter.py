pr = lambda x: x >= 1 and all(x % y != 0 for y in range(2, int(x**0.5) + 1))

primes = []

while True:
    num = input()
    if num == "":
        break
    else:
        primes.append(int(num))

filtered = filter(pr, primes)

for x in filtered:
    print(x)
    