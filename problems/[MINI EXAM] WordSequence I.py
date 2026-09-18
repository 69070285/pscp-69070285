"""[MINI EXAM] WordSequence I"""

def main():
    """Main Function"""
    text = input()

    for i in range(len(text)):
        print(text[:i + 1])

main()
