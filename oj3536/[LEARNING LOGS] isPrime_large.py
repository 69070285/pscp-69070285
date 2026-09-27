"""[LEARNING LOGS] isPrime_large"""

def main():
    """Main Function"""
    target = int(input())

    for check in range(2, int(target**0.5) + 1):
        if not target % check:
            return print("NO")

    return print("NO" if target <= 1 else "YES")

main()
