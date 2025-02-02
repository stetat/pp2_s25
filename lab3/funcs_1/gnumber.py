import random

name = str(input("Hello! What is your name?\n"))
num = random.randint(1,21)
count = 0

print(f"Well, {name}, I am thinking of a number between 1 and 20.\n")

while True:
    
    count+=1
    guess = int(input("Take a guess.\n"))
    if( guess < num ):
        print("Your guess is too low.\n")
        continue

    elif( guess > num):
        print("Your guess is too high.\n")
        continue

    else:
        if( count == 1):
            print(f"Good job, {name}! You guessed my number in 1 guess!")
            
        else:
            print(f"Good job, {name}! You guessed my number in {count} guess!")
        break
    
    
