"""List Prime (Sieve of Eratosthenes)"""

def main():
    """Main Function"""
    target = int(input())
    primes = []

    for num in range(2, target + 1):
        is_prime = True
        for check in range(2, int(num**0.5) + 1):
            if not num % check:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    if target in primes:
        print("Yes")
        print(*primes)
    else:
        print("No")

main()
