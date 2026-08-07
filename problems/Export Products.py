"""Export Products"""

def main():
    """Main Function"""
    amount = int(input())
    sum_num = 0
    even = 0
    odd = 0

    for _ in range(amount):
        number = int(input())
        sum_num += number

        if not number % 2:
            even += 1
        else:
            odd += 1

    print(f"SUM {sum_num}")
    print(f"EVEN {even}")
    print(f"ODD {odd}")

main()
