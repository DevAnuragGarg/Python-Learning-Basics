options = """Please choose your option from the list below:
1.\tLearn python
2.\tLearn java
3.\tGo swimming
4.\tHave dinner
5.\tGo to bed
0.\tExit"""

while True:
    choice = input()

    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}".format(choice))
