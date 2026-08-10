"""[LEARNING LOGS] Gift And Thief"""

def main():
    """Main Function"""
    amount, step, thief = map(int, input().split())
    result = 0
    start = 1

    while True:
        if start == thief:
            result += 1
            break
        if start == 1 and result:
            break
        start = (start + step) % amount
        result += 1

    print(result)

main()
