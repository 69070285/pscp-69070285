"""[MIDTERM] Stats"""

def main():
    """Main Function"""
    amount = int(input())
    least = 2e9
    most = -2e9
    total = 0

    for _ in range(amount):
        number = int(input())
        if number > most:
            most = number
        if number < least:
            least = number
        total += number

    print(f"MIN: {least:.3f}")
    print(f"MAX: {most:.3f}")
    print(f"AVG: {total / amount:.3f}")

main()
