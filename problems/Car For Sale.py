"""Car For Sale"""

def main():
    """Main Function"""
    min_price, max_per = 2e9, -2e9
    amount = int(input())
    cars = [list(map(int, input().split())) for _ in range(amount)]

    for price, performance in cars:
        if price < min_price and performance > max_per:
            min_price, max_per = price, performance

    if min_price == cars[-1][0] and max_per == cars[-1][1]:
        print(len(cars) - 1)
    else:
        eww = 0
        max_per = cars[-1][1]
        for i in cars[::-1]:
            if i[1] < max_per:
                eww += 1
        print(len(cars) - eww)

main()
