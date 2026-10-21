"""Stair"""

def main():
    """Main Function"""
    limit, height = int(input()), [int(input()) for _ in range(int(input()))]
    i, count = 0, 0

    while i < len(height):
        start = limit
        while i < len(height) and start - height[i] >= 0:
            start -= height[i]
            i += 1
        if start == limit:
            return print("NO")
        count += 1

    return print(count)

main()
