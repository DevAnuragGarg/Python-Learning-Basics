# formatting
menu = [
    ["egg", "bacon"],
    ["egg", "bacon", "sausage"],
    ["egg", "spam"],
    ["egg", "spam", "tomato"],
    ["egg", "spam", "tomato", "spam", "tomato"],
]

for meal in menu:
    if "spam" in meal:
        print("Yeah, not there")
    else:
        print("{0} has the spam score of {1}"
              .format(meal, meal.count("spam")))

# challenge: print all the values just not spam
for meal in menu:
    if "spam" in meal:
        meal.remove("spam")
    print(meal)
