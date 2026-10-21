"""08.00 - B RNG"""

import json

def main():
    """Main Function"""
    num_list, need, step = json.loads(input()), int(input()), int(input())
    most, start = -2e9, 0

    while start < len(num_list):
        total, i = 0, start
        for _ in range(need):
            total += num_list[i]
            i = (i + step) % len(num_list)
        if total > most:
            most = total
        start += 1

    print(most)

main()
