"""Rabbit Fever"""

from math import dist, floor

def main():
    """Main Function"""
    row, col = map(int, input().split())
    rab_row, rab_col = map(int, input().split())
    amount = int(input())
    rab_fever = [list(map(int, input().split())) for _ in range(amount)]
    fever = {0: 100, 1: 60, 2: 20, 3: 0}
    all_rabbit = []

    for r in range(row):
        for c in range(col):
            min_dist = min(floor(dist([r, c], f)) for f in rab_fever)
            all_rabbit.append(fever[3 if min_dist > 3 else min_dist])

    print(all_rabbit.count(0))
    print(f"{all_rabbit[rab_row * col + rab_col]}%")

main()
