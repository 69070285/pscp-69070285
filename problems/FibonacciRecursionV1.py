"""FibonacciRecursionV1"""

def fibonacci(n):
    """Fibonacci Calculate"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """Main Function"""
    print(fibonacci(int(input())))

main()
