"""LineSorting"""

def main():
    """Main Function"""
    text = sorted([input() for _ in range(int(input()))],key=len)
    print("\n".join(text))

main()
