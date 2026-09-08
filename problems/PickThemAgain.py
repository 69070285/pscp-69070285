"""PickThemAgain"""

def main():
    """Main Function"""
    result = []
    numbers = list(map(int, input().split()))[::-1]
    result.extend([i for i in numbers if not i % 3 or not i % 5])

    if not result:
        print("Nope")
    else:
        for i in result:
            print(i)

main()
