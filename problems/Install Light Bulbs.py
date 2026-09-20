"""Install Light Bulbs"""

def main():
    """Main Function"""
    amount = int(input())
    light_bulbs = sorted([int(input()) for _ in range(amount)])
    total = sum((l + sum(light_bulbs[:index])) * 2 for index, l in enumerate(light_bulbs))
    print(total)

main()
