age = int(input("How old are you? "))

if 16 <= age < 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# here in place we can use ranges
if age in range(16, 65):
    print("Enjoy your free time")
else:
    print("Have a good day at work")
