"""[ MINI EXAM ] Cat in the Bag"""

def main():
    """Main Function"""
    cat = []
    while True:
        bag = input().lower()
        if bag == "-1":
            break
        if "cat" in bag:
            cat.append(bag)

    print(f"The number of cat in bag {len(cat)}")
    print(f"List of cat {cat}")

main()
