"""[MINI EXAM] Calendar"""

def main():
    """Main Function"""
    day = int(input())
    month = int(input())
    year = int(input())
    total = day + (month * 30) + (year * 360)
    left = 2 + (10 * 30) + (2569 * 360)

    if total >= left:
        print("0")
    else:
        print(left - total)

main()
