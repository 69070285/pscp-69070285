"""Star Shape"""

def main():
    """Main Function"""
    size = int(input())

    for _ in range(3):
        print("*" * size if size >= 1 else "")
        size -= 2

main()
