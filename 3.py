import random

chosen = random.randint(0,100)
guessed = 0

print("Your default guessed number is zero.\n")

while guessed != chosen:
    if guessed > chosen:
        guessed = int(input("Please lower your guess: "))
        if guessed == chosen:
            print("Congratulations! You guessed correctly.")
    elif guessed < chosen:
        guessed = int(input("Please increase your guess: "))
        if guessed == chosen:
            print("Congratulations! You guessed correctly.")