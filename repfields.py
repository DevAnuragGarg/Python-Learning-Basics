age = 24
# print("My age is " + 3), you can't concatenate string with int
print("My age is " + str(age) + " years")  # you can use str to convert anything to string
print("My age is {0} years".format(age))
print(
    "There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(31, "January", "March", "May", "Jul", "Aug", "Oct",
                                                                     "Dec"))
