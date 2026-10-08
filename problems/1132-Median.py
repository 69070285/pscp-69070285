"""1132-Median"""

def main():
    """Main Function"""
    numbers = sorted(map(float, input().split(", ")))

    if len(numbers) % 2:
        print(f"{numbers[len(numbers) // 2]:.2f}")
    else:
        print(f"{(numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2:.2f}")

main()
