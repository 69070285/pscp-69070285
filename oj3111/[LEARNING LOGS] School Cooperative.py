"""[LEARNING LOGS] School Cooperative"""

def main():
    """Main Function"""
    member = input()
    amount = int(input())
    total = 0

    for _ in range(amount):
        item = float(input())
        total += item

    match member:
        case "Y":
            total = total * 0.95
        case "N" if total >= 500:
            total = total * 0.97

    total += 0.001
    print(f"{total:.2f}")

main()
