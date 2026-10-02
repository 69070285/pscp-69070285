"""Ramen Bowl"""

def main():
    """Main Function"""
    amount = int(input())
    bowls = [int(input()) for _ in range(amount)]
    print(max(bowls.count(b) for b in set(bowls)))

main()
