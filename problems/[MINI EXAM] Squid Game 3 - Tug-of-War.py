"""[MINI EXAM] Squid Game 3 - Tug-of-War"""

def main():
    """Main Function"""
    a = sum(int(input()) for _ in range(10))
    b = sum(int(input()) for _ in range(10))

    if a - b < 0:
        print("A")
    elif a - b > 0:
        print("B")
    else:
        print("AB")

main()
