"""[LEARNING LOGS] School Cooperative"""

def main():
    """Main Function"""
    member = input()
    amount = int(input())
    total = 0
    result = 0
    decimal = 0

    for _ in range(amount):
        item = float(input())
        total += item

    match member:
        case "Y":
            result = total * 0.95
        case _:
            if total >= 500:
                result = total * 0.97
            else:
                result = total

    decimal = f"{result:.3f}"
    if decimal[-1] == "5":
        result += 0.001
    print(f"{result:.2f}")

main()
