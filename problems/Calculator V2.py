"""Calculator V2"""

def main():
    """Main Function"""
    target = int(input())
    press = 0
    length = 1
    start = 1

    while start <= target:
        stop = min(target, start * 10 - 1)
        count = stop - start + 1
        press += count * length
        start *= 10
        length += 1

    print("1" if target == 1 else press + target)

main()
