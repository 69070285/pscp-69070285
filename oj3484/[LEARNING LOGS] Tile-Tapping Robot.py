"""[LEARNING LOGS] Tile-Tapping Robot"""

def main():
    """Main Function"""
    size, cost = map(int, input().split())
    tile = [list(map(int, input().split())) for _ in range(size)]
    row_broke = [[sum(1 for col in t if col > 0), sum(t)] for t in tile]
    col_spot = []
    col_point = []

    for col in range(size):
        spot = 0
        point = 0
        for t in tile:
            if t[col] > 0:
                spot += 1
                point += t[col]
        col_spot.append(spot)
        col_point.append(point)

    for row, t in enumerate(tile):
        print(*t + row_broke[row])
    print(*col_spot)
    print(*col_point)
    print(f"{sum(col_spot)} {sum(col_point)} {sum(col_point) * cost:.2f}")

main()
