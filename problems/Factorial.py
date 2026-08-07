"""Factorial"""

def main():
    """Main Function"""
    number = int(input())
    total = 1

    for i in range(1, number + 1):
        total *= i

    print(total)

main()
