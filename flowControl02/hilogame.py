low = 1
high = 1000
print("Guess any value between {} and {}".format(low, high))
print("Press ENTER to start the game")
input()
mid = 0
numberOfGuesses = 0
while low != high:
    mid = int((low + high) / 2)
    print("Is the value {} guessed is right? Should i guess higher or lower".format(mid))
    guessedChar = input()
    numberOfGuesses += 1

    if guessedChar == 'h':
        low = mid + 1
    elif guessedChar == 'l':
        high = mid - 1
    elif guessedChar == 'c':
        print("Number of guesses required: {}".format(numberOfGuesses))
        break
    else:
        print("Please enter h, l or c")
else:
    print("You thought of {} number in {} guesses".format(low, numberOfGuesses))
