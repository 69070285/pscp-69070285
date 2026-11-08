"""[MINI EXAM] Members"""

def main():
    """Main Function"""
    a, b = set(input().split()), set(input().split())
    print(*(sorted(a - b) if a - b else "-"))
    print(len(a | b))

main()
