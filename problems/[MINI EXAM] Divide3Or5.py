"""[MINI EXAM] Divide3Or5"""

def main():
    """Main Function"""
    stop = int(input())
    result = sum(i for i in range(stop + 1) if not i % 3 or not i % 5)
    print(result)

main()
