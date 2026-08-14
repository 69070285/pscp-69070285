"""Triangle"""

def main():
    """Main Function"""
    amount = int(input())

    for i in range(1, amount + 1):
        if i in (1, 2, amount):
            print("0" * i, end="")
        else:
            print("0" + "1" * (i - 2) + "0", end="")
        print()

main()
