"""Print Symbol"""

def main():
    """Main Function"""
    number = int(input())

    for i in range(1, number + 1):
        if not i % 5:
            print("X", end="")
        else:
            print("*", end="")

main()
