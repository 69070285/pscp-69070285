"""[LEARNING LOGS] Pad Thai"""

def main():
    """Main Function"""
    ingredients = {
        "Pad Thai Sauce": False, "Tofu": False, "Pickle Turnip": False, "Shrimp": False,
        "Bean Sprouts": False, "Noodle": False, "Chives": False, "Lime": False, "Egg": False,
        "Oil": False, "Peanuts": False
    }
    taste = {"Sweet": False, "Sour": False, "Salty": False}

    while True:
        i = input()
        if i == "Cook":
            break
        ingredients[i] = True

    while True:
        t = input()
        if t == "End":
            break
        taste[t] = True

    if len(ingredients) > 11:
        print("This is not Pad Thai!!!")
    elif not all(ingredients.values()):
        print("This is bad!")
    elif all(ingredients.values()) and not all(taste.values()) or len(taste) > 3:
        print("Not Bad...")
    else:
        print("Delicious!")

main()
