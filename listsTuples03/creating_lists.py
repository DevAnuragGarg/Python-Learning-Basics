empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# creating lists using concatenating two lists
numbers = even + odd
print(numbers)

# using a function that returns a list
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# what this will produce
digits = sorted("03524849")
print(digits)  # it will produce list of strings containing single digit

# creating a list directly
digit_list = list("45373992")
print(digit_list)

# we can use list keyword for creating the duplicate list
numbers_list = list(numbers)
print(numbers_list)
print(numbers)

# we will check if both are the same lists
print(numbers is numbers_list)

# check if the items in two lists are same
print(numbers == numbers_list)

# copying the list using slice
more_numbers = numbers[:]
print(more_numbers)

# copying the list using copy method
copy_numbers = numbers.copy()
print(copy_numbers)
