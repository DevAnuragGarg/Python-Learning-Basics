for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))
# it means it will take these many columns

print()
# left aligning
for i in range(1, 13):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print()
# center aligning
for i in range(1, 13):
    print("No. {0:2} squared is {1:^4} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()
print("Pi is approximately {0:12}".format(22 / 7))  # prints 15 decimals generic
print("Pi is approximately {0:12f}".format(22 / 7))  # 6 digit after the decimal
print("Pi is approximately {0:12.50f}".format(22 / 7))  # 50 point after the decimal
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))

print()
# not mentioning anything, only the width
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

name = "Anurag Garg"
age = 24
print(name + f" is {age} years old")  # formatting
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
