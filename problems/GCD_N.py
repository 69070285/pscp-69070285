"""GCD_N"""

from math import gcd

def main():
    """Main Function"""
    amount = int(input())
    numbers = [int(input()) for _ in range(amount)]
    print(gcd(*numbers))

main()
