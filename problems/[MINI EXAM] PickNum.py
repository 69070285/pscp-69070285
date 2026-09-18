"""[MINI EXAM] PickNum"""

def main():
    """Main Function"""
    pos = 0
    neg = 0
    zero = 0
    numbers = list(map(int, input().split()))

    for i in numbers:
        if not i:
            zero += 1
        elif i > 0:
            pos += 1
        else:
            neg += 1

    print(f"Positive: {pos}")
    print(f"Negative: {neg}")
    print(f"Zero: {zero}")

main()
