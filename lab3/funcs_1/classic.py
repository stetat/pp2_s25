numhead = int(input('enter heads amount: '))
numlegs = int(input('enter legs amount: '))

def solve(numhead, numlegs):

    rabbits = numlegs/2 - numhead
    chickens = numhead - rabbits


    return f"chickens: {int(chickens)}\nrabbits: {(int(rabbits))}"

print(solve(numhead, numlegs))