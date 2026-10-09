"""3nPlus1"""

def main():
    """Main Function"""
    while True:
        number = int(input())
        if not number:
            break

        count = 1
        while number != 1:
            count += 1
            if not number % 2:
                number //= 2
            else:
                number = number * 3 + 1
        print(count)

main()
