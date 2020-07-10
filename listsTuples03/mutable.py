shopping_list = ["milk",
                 "bread",
                 "rice",
                 "pasta",
                 "eggs"]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(id(shopping_list))
print(id(another_list))
