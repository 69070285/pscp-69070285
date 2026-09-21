"""Impact Zone"""

def main():
    """Main Function"""
    amount = int(input())
    point = [list(map(int, input().split())) for _ in range(amount)]
    start_x, stop_x = (point[0][0] - point[0][2]), (point[0][0] + point[0][2])
    start_y, stop_y = (point[0][1] - point[0][2]), (point[0][1] + point[0][2])

    for x in range(start_x, stop_x + 1):
        for y in range(start_y, stop_y + 1):
            for i, p in enumerate(point):
                if pow(x - p[0], 2) + pow(y - p[1], 2) == pow(p[2], 2):
                    if i == amount - 1:
                        print(x, y)
                        return
                    continue
                break

main()
