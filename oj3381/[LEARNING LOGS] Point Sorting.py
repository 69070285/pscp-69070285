"""[LEARNING LOGS] Point Sorting"""

def main():
    """Main Function"""
    amount = int(input())

    for _ in range(amount):
        pair = int(input())
        point = [tuple(map(int, input().split())) for _ in range(pair)]
        point.sort(key=lambda p: (p[0] + p[1], -p[1]))

        for x, y in point:
            print(x, y)

main()
