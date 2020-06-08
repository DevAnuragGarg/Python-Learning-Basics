# there is nothing as such blocks, in place python use indentation

for i in range(1, 13):  # : depicts move to next indented line
    print("No. {} square is {} and cube is {:4}".format(i, i ** 2, i ** 3))
    print("#" * 10)
print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# for the block : is put at the end and the next line start with indentation
if age >= 18:
    print("You are old enough to vote")
elif age == 12:
    print("You are of age 12")
else:
    print("Please be 18 or more")
