"""MissingNumber"""

def main():
    """Main Function"""
    numbers = []
    stop = int(input())
    while True:
        number = int(input())
        if not number:
            break
        numbers.append(number)

    for i in range(1, stop + 1):
        if i not in numbers:
            print(i)

main()
