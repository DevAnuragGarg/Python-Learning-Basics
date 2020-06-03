letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]  # it will go from backward to forward only when having negative steps
print(backwards)
backwards = letters[25::-1]  # it will go from backward to forward only when having negative steps
print(backwards)
backwards = letters[::-1]
print(backwards)

# Assignments
# print qpo
print(letters[16:13:-1])
# print edcba
print(letters[4::-1])
# print last 8 char in reverse order
print(letters[:-9:-1])
print(letters[:17:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])  # if string is empty this will not give error
print(letters[0])  # if the string is empty then it will give error

# Phyton 3 has 5 sequence built in:
# String type
# List type
# Tuple type
# Range type
# Bytes and ByteArray type
# Whatever we can do with str Sequence type can be done with other sequence type
# Exception: Not all sequence types can be concatenated or multiplied. Ex: Range
