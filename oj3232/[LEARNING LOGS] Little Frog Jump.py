"""[LEARNING LOGS] Little Frog Jump"""

def main():
    """Main Function"""
    jump, target = map(int, input().split())
    count = 0

    while jump > 0:
        count += 1
        target -= jump
        jump -= 2
        if target <= 0:
            break

    if target <= 0:
        print(count)
    else:
        print("-1")

main()
