# deleting the value from the list
data = [4, 5, 105, 110, 146, 159, 163, 179, 183, 200, 256, 323, 435]

min_valid = 100
max_valid = 200

# we can use the range to travel back
top_index_value = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value > max_valid or value < min_valid:
        del (data[top_index_value - index])
        print(top_index_value - index, value)

print(data)
