answer = 5
print("Please guess the number between 1 and 10: ")
guess = int(input())  # input returns string always, converting it to int

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess low")
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("Correct answer")

if guess != answer:
    if guess > answer:
        print("Please guess lower")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Correct answer, you guessed it now")
    else:
        print("Sorry, you have again guessed wrongly")
else:
    print("Correct answer")
