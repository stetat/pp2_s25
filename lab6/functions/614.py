import time, math

n = int(input("enter some number: "))
t = int(input("how long do we wait? (ms): "))

time.sleep(t/1000)

print(f"we waited {t} milliseconds\nsquare root of {n} is {round(pow(n, 0.5), 3)}")
