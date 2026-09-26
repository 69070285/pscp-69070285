"""[ MINI EXAM ] Dart"""

from math import sqrt

def main():
    """Main Function"""
    result = []
    amount = int(input())

    for _ in range(amount):
        x, y = map(int, input().split())
        method = sqrt(x**2 + y**2)
        if method <= 2:
            result.append(5)
        elif method <= 4:
            result.append(4)
        elif method <= 6:
            result.append(3)
        elif method <= 8:
            result.append(2)
        elif method <= 10:
            result.append(1)

    print(sum(result))

main()
