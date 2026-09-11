"""Difference"""

def main():
    """Main Function"""
    amount_a = int(input())
    amount_b = int(input())
    a = {int(input()) for _ in range(amount_a)}
    b = {int(input()) for _ in range(amount_b)}

    result = sorted(list(a - b))
    print(*result)

main()
