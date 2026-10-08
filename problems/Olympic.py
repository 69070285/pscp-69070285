"""Olympic"""

def main():
    """Main Function"""
    amount = int(input())
    data = []

    for _ in range(amount):
        name, gold, silver, bronze = input().split()
        gold, silver, bronze = int(gold), int(silver), int(bronze)
        data.append([name, gold, silver, bronze, gold + silver + bronze])

    data.sort(key=lambda d: (-d[1], -d[2], -d[3], d[0]))

    for i, d in enumerate(data):
        if i and data[i][1:] == data[i - 1][1:]:
            print(stay, *d)
            continue
        stay = i + 1
        print(i + 1, *d)

main()
