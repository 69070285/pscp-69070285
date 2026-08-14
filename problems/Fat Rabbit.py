"""Fat Rabbit"""

def main():
    """Main Function"""
    amount = int(input())
    max_name = ""
    max_weight = -2e9
    overweight = 0

    for _ in range(amount):
        data = input().split()
        name = data[0]
        weight = int(data[1])

        if weight > 15:
            overweight += 1
        if weight > max_weight:
            max_name = name
            max_weight = weight

    print(overweight)
    print(max_name)

main()
