"""FibonacciRecursionV2"""

def fibonacci(n):
    """Fibonacci Calculate"""
    if not n:
        return (0, 1)

    a, b = fibonacci(n // 2)
    c = a * (2 * b - a)
    d = a * a + b * b
    return (c, d) if not n % 2 else (d, c + d)

def main():
    """Main Function"""
    print(fibonacci(int(input()))[0])

main()
