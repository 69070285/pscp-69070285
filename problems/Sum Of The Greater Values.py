"""Sum Of The Greater Values"""

def main():
    """Main Function"""
    amount = int(input())
    all_greater = []
    all_greater_str = []

    for _ in range(amount):
        first = int(input())
        second = int(input())
        all_greater.append(max(first, second))
        all_greater_str.append(str(max(first, second)))

    if len(all_greater) == 1:
        print(all_greater[0])
    else:
        print(" + ".join(all_greater_str), "=", (sum(all_greater)))

main()
