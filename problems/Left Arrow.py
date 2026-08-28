"""Left Arrow"""

def main():
    """Main Function"""
    width = int(input())
    height = int(input())
    center = height // 2

    for i in range(height):
        dist = abs(i - center)
        print(" " * dist + "*" * width)

main()
