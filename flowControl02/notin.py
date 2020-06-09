activity = input("What would you like to do today?")

if "cinema" not in activity.casefold():  # casefold will make all the characters lowercase
    print("But I want to go to cinema")

# Challenge
age = int(input("Please enter your age: "))
if 18 <= age < 31:
    print("Welcome them to the holiday")
else:
    print("Refusing them to entry")
