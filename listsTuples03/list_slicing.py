computer_parts = ["mouse",
                  "keyboard",
                  "monitor",
                  "computer",
                  "mouse_mat"
                  ]
print(computer_parts)

computer_parts[3] = "trackball"
print(computer_parts)

# slicing will replace the items with the content of the iterable : String
computer_parts[3:] = "usb_cable"
print(computer_parts)
