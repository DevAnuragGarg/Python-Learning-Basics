empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

# this will put lists into a list
numbers = [even, odd]
print(numbers)

for number_list in numbers:
    for number in number_list:
        print(number)
