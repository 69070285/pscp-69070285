"""[MINI EXAM] Noodle"""

def main():
    """Main Function"""
    price = int(input())
    money = int(input())

    if not price - money:
        print("Good!")
    elif money - price > 0:
        print(money - price)
    else:
        print("Need more cash!")

main()
