birdName = "Norwegian Blue"
print()
string = "we win"
for i in range(len(string)):
    print(string[i])

print()
print(birdName[-1])
print(birdName[-14])

print()
print(birdName[0:6])  # 6th is not included
print(birdName[0:9])
print(birdName[:9])
print(birdName[10:])
print(birdName[:])

print(birdName[-4:2])  # you cannot go back from starting to end
print(birdName[-4:-2])
print(birdName[-4:12])

# steps
print(birdName[0:6:2])  # in steps of 2
print(birdName[1::5])

numbers = "9,456:469;985 217,463;863"
separators = numbers[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in numbers).split()
print([int(val) for val in values])
