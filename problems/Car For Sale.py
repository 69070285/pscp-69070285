"""Car For Sale"""

def main():
    """Main Function"""
    max_performance = -1
    low_performance = 0
    amount = int(input())
    cars = [list(map(int, input().split())) for _ in range(amount)]

    for _, performance in cars[::-1]:
        if performance < max_performance:
            low_performance += 1
        else:
            max_performance = performance

    print(low_performance)

main()
