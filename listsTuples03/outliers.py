# deleting the value from the list
data = [4, 5, 105, 110, 146, 159, 163, 179, 183, 200, 256, 323, 435]
print(data)

# deleting the items first 2
# del data[0:2]
print(data)

# this will not do anything as it is out of scope
del data[16:]
print(data)

min_valid = 100
max_valid = 200

# for index, value in enumerate(data):
#     if value < min_valid or value > max_valid:
#         del data[index]
#         # can't manipulate the loop values, below don't work
#         # index = -1
#
# print(data)

# remove the values below min_valid value
stop = 0
for index, value in enumerate(data):
    if value > min_valid:
        stop = index
        break

del (data[:stop])
print(data)

# remove the values above miax_valid value
start = 0
for index, value in enumerate(data):
    if value > max_valid:
        start = index
        break

del (data[start:])
print(data)

# we can use the range to travel back
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index
        break

del (data[start:])
print(data)
