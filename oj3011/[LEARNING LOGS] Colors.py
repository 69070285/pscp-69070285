"""[LEARNING LOGS] Colors"""

first_color = input().lower()
second_color = input().lower()

if first_color in ("red", "yellow", "blue") and second_color in ("red", "yellow", "blue"):
    if (first_color, second_color) in [("red", "yellow"), ("yellow", "red")]:
        print("Orange")
    elif (first_color, second_color) in [("red", "blue"), ("blue", "red")]:
        print("Violet")
    elif (first_color, second_color) in [("blue", "yellow"), ("yellow", "blue")]:
        print("Green")
    elif first_color == second_color:
        print(first_color.title())
else:
    print("Error")
