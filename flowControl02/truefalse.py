if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name:            # it checks automatically if the name is empty or not
    print("Hello, {}".format(name))
else:
    print("Are you the main with no name?")
