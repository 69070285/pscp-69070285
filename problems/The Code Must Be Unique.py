"""The Code Must Be Unique"""

def main():
    """Main Function"""
    _ = int(input())
    code = list(map(int, input().split()))
    unique = sorted([c for c in code if code.count(c) == 1])
    print(*unique)

main()
