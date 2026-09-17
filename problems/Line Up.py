"""Line Up"""

def main():
    """Main Function"""
    _, _ = map(int, input().split())
    height = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    result = []

    for i in queue:
        tallest = max(height[:i]) if i != 1 else 0
        current = height[i - 1]
        if current >= tallest:
            result.append(0)
        else:
            add = tallest - current + 1
            result.append(add)

    print(*result, sep="\n")

main()
