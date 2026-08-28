"""Right Arrow"""

def main():
    """Main Function"""
    width = int(input())
    height = int(input())
    center = height // 2

    for i in range(center + 1):
        print(" " * i + "*" * width)
    for i in range(1, center + 1):
        print(" " * (center - i) + "*" * width)

main()
