"""Online Game Scoring System"""

def main():
    """Main Function"""
    base = float(input())
    bonus = float(input())
    day = int(input())
    total = base + bonus
    if day > 3:
        total *= 1.5
    special = 0

    if total >= 1500:
        level = 5
    elif total >= 1000:
        level = 4
    elif total >= 500:
        level = 3
    elif total >= 200:
        level = 2
    else:
        level = 1

    if level == 5 and day >= 7:
        special = 99
    elif level == 4 and bonus > 300:
        special = 88

    print(int(total))
    print(level)
    print(special)

main()
