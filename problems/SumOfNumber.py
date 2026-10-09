"""SumOfNumber"""

def main():
    """Main Function"""
    target = int(input())
    total = 0

    while total != target:
        number = int(input())
        if number == -1:
            break
        total += number

    print(total)

main()
