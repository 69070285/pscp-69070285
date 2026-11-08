"""Island"""

def main():
    """Main Function"""
    row, col = map(int, input().split())
    spot, island = [[0] * (col + 2)], 0
    for _ in range(row):
        spot.append([0] + [int(s) for s in input().split()] + [0])
    spot.append([0] * (col + 2))
    around = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1)]

    for r, c in [(r, c) for r in range(1, row + 1) for c in range(1, col + 1)]:
        if not spot[r][c]:
            continue
        island += 1
        spot[r][c] = 0
        stack = [(r, c)]
        while stack:
            cr, cc = stack.pop()
            for dr, dc in around:
                nr, nc = cr + dr, cc + dc
                if spot[nr][nc]:
                    spot[nr][nc] = 0
                    stack.append((nr, nc))

    print(island)

main()
