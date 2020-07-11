# enumeration
available_parts = ['monitor', 'mouse mat', 'mouse', 'keyboard', 'computer']
current_choice = "-"
computer_parts = []
# comprehensions
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        if available_parts[int(current_choice) - 1] in computer_parts:
            computer_parts.remove(available_parts[int(current_choice) - 1])
        else:
            computer_parts.append(available_parts[int(current_choice) - 1])
    else:
        print("Please add options from the list below:")
        # enumeration
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
    current_choice = input()

print(computer_parts)
