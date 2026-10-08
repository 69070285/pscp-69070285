"""Bus Seat"""

def main():
    """Main Functiion"""
    row = int(input())
    column = int(input())
    seat = int(input())
    bus = ["XX" if i == seat else f"{i:02d}" for i in range(1, (row * column) + 1)]

    for count, i in enumerate(range(row - 1, -1, -1)):
        if count > 0 and not count % 2:
            print()
        print(" ".join(bus[i::row]))

main()
