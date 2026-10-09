"""How Many"""

def main():
    """Main Function"""
    boys, girls= 0, 0

    while True:
        card = input()
        if int(card) < 0:
            break
        if card[-1] in "1 3 5 7 9":
            boys += 1
        else:
            girls += 1

    print(boys, girls, boys + girls)

main()
