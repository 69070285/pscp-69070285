"""Cave Explorer"""

def main():
    """Main Function"""
    amount = int(input()) - 1
    cave = list(map(int, input().split()))
    target = cave.index(2)
    command = input()

    for c in command:
        pos = cave.index(1)
        if pos == target:
            break

        if c == "R" and pos < amount:
            cave[pos + 1] = 1
            cave[pos] = 0
        elif c == "L" and pos > 0:
            cave[pos - 1] = 1
            cave[pos] = 0

    print(*cave)

main()
