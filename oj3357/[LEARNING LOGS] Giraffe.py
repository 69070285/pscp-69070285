"""[LEARNING LOGS] Giraffe"""

def main():
    """Main Function"""
    amount = int(input()) + 2
    giraffe = [0 if not i or i == amount - 1 else int(input()) for i in range(amount)]
    chill = sum(giraffe[i - 1] < giraffe[i] > giraffe[i + 1] for i in range(1, amount - 1))
    print(chill)

main()
