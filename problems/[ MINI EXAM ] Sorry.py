"""[ MINI EXAM ] Sorry"""

def main():
    """Main Function"""
    storage = []
    while True:
        order = input()
        if order == "End":
            break
        if order == "Sorry":
            storage.pop()
        else:
            storage.append(order)

    print(", ".join(storage))

main()
