# sequence can be iterable e.g. String
# difference between strings and lists: Strings are immutable
# but contents of the lists can be changed
computer_parts = ["mouse",
                  "keyboard",
                  "monitor",
                  "computer",
                  "mouse_mat"
                  ]
for part in computer_parts:
    print(part)

print()
# indexing
print(computer_parts[2])

# slicing
print(computer_parts[0:3])
print(computer_parts[-1])
