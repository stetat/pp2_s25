import datetime

tdy = datetime.datetime.now()
yst = tdy - datetime.timedelta(days=1)
tmr = tdy + datetime.timedelta(days=1)

print(f"{yst}\n{tdy}\n{tmr}")