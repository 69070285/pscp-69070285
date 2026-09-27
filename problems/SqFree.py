"""SqFree"""

def main():
    """Main Function"""
    amount = int(input())
    count = 0

    for a in range(1, amount + 1):
        for b in range(2, int(a**0.5) + 1):
            if not a % (b * b):
                break
        else:
            count += 1

    print(count)

main()
