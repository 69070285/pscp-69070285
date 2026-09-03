"""Life Balance"""

def main():
    """Main Function"""
    amount = int(input())
    over = 0
    under = 0

    for _ in range(amount):
        hour = int(input())
        if hour > 18:
            over += 1
        else:
            under += 1

    if over - under <= 1:
        print(amount)
    else:
        print(amount + (over - under - 1))

main()
