# a list is ordered sequence of values, enclosed in square brackets
shopping_list = ["milk", "pasta", "spam", "eggs"]

for item in shopping_list:
    if item != "spam":
        print("Buy " + item)

print()

# similar case can be handled using continue
for item in shopping_list:
    if item == "spam":
        break
    print("Buy " + item)

print()

# using the break statement
item_to_find = "spam"
found_at = None  # just like null in java, if we haven't given any value to this
# variable then it will crash, so better to declare it as NONE here
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

# all the above code can easily be done as below
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

# putting up the null check
if found_at is not None:
    print("Found the item {0} at position {1}".format(item_to_find, found_at))
else:
    print("{0} not found".format(item_to_find))
