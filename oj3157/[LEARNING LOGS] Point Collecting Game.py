"""[LEARNING LOGS] Point Collecting Game"""

def main():
    """Main Function"""
    amount = int(input())
    total = 0

    for _ in range(amount):
        command = input()
        match command:
            case "+":
                total += 10
            case _:
                total -= 5

    print(total)

main()
