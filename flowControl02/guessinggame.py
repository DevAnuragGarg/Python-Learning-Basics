# need to import random to fetch the random values
import random

# random int function of random in which both the values are included
highest = 10
answer = random.randint(1, highest)
print("Please guess the number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    guess = int(input())  # input returns string always, converting it to int

    if guess == 0:
        break

    if guess != answer:
        if guess > answer:
            print("Please guess lower")
        else:
            print("Please guess lower")
    else:
        print("Correct answer, you guessed it now")
        break
