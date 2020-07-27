# join
flowers = [
    "Dadoffil",
    "Sunflower",
    "Lilly",
    "Rose",
    "Iris",
    "Tiger lilly",
    "Lavender"
]

# join is a method of str class and it separates the string value in
# the list using a separator. We don't need to use the for loop for
# iteration, join will iterate itself over the list

# all the item need to be string if you want to join, otherwise it will crash
separator = " | "
output = separator.join(flowers)
print(output)
