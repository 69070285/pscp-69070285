"""Array 2D Check"""

def main():
    """Main Function"""
    table = [list(map(int, input().split())) for _ in range(5)]

    for row in range(5):
        for col in range(5):
            sum_col = sum(r[col] for r in table)
            sum_row = sum(table[row])
            if sum_col % 2 and sum_row % 2:
                print(row, col)
                return

    print(-1, -1)

main()
