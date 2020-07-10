result = True
another_result = result
# id() function returns a unique id for the specified object.
print(id(result))
print(id(another_result))

result = False
print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
