"""[ MINI EXAM ] Adventurer's Backpack"""

def main():
    """Main Function"""
    bag = input()
    add = input()

    if bag == "Empty":
        bag = []
    else:
        bag = bag.split(",")

    if add == "Stone":
        print("I don't need this!")
    else:
        while len(bag) >= 5:
            bag.pop(0)
        bag.append(add)

    print(bag)

main()
