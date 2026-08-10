"""[LEARNING LOGS] Find Prime Numbers"""

def main():
    """Main Function"""
    start, stop = map(int, input().split())
    prime = []

    for number in range(start, stop + 1):
        for check in range(2, number + 1):
            if check == number:
                prime.append(str(number))
            elif not number % check:
                break

    if prime:
        print(" ".join(prime))
    print(f"Total primes: {len(prime)}")

main()
