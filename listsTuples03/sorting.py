pangram = "The quick brown fox jumps over the lazy dog"
# it creates the list from the iterables
letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 31., 9.1, 1.6]
# here we are passing the list and get the new list in return
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# the sort function sort the original list and doesn't create new list
numbers.sort()
print(numbers)

# added a argument key which make the capital T to be shown with the small ones
missing_letter = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "Micheal"]
# this will print the names starting with small letters at the end
names.sort()

# this will print the names starting with small letters at the end
names.sort(key=str.casefold)

print(names)
