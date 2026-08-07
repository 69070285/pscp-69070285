"""Stroll Through The Festival"""

def main():
    """Main Function"""
    command = input()
    n = command.count("N")
    s = command.count("S")
    w = command.count("W")
    e = command.count("E")

    print(e - w, n - s, abs(n - s) + abs(e - w))


main()
