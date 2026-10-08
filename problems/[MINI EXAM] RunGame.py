"""[MINI EXAM] RunGame"""

def main():
    """Main Function"""
    try:
        x = 0
        distance = 0
        item = list(map(int, input().split()))

        for i in item:
            distance += abs(x - i)
            x = i
    except EOFError:
        pass

    print(distance)

main()
