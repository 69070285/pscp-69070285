"""Kangaroo"""

def main():
    """Main Function"""
    spot = [int(input()) for _ in range(3)]
    print(max(spot[2] - spot[1], spot[1] - spot[0]) - 1)

main()
