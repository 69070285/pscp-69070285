"""Coffee Shop Sales Analysis"""

def main():
    """Main Function"""
    amount = int(input())
    all_num = []

    for _ in range(amount):
        number = int(input())
        all_num.append(number)

    print(sum(all_num))
    print(max(all_num))
    print(min(all_num))
    print(f"{sum(all_num) / amount:.1f}")

main()
