available_exists = ["north", "south", "east", "west"]
choose_exit = ""
while choose_exit.casefold() not in available_exists:
    choose_exit = input("Please choose a direction: ")
    if choose_exit.casefold() == "quit":
        print("Game over")
        break

print("Aren't you glad you got out of there")

# while loop you don't know for how many iterations you want to run the loop,
# one of the application of while is reading streams until no data is left

# for loop you know for how many iterations you want to run the loop
print()

i = 1
while i < 21:
    if i % 3 == 0 or i % 5 == 0:
        i += 1
        continue
    else:
        print(i)
    i += 1
