"""08.00 - B RNG"""

import json

def main():
    """Main Function"""
    num_list, need, step = json.loads(input()), int(input()), int(input())
    most, size = -2e9, len(num_list)
    seen = [False] * size

    for start in range(size):
        if not seen[start]:
            cycle, i = [], start

            while not seen[i]:
                seen[i] = True
                cycle.append(num_list[i])
                i = (i + step) % size

            length = len(cycle)
            full, rem = divmod(need, length)
            pre = [0]

            for v in cycle + cycle:
                pre.append(pre[-1] + v)

            best = max(pre[j + rem] - pre[j] for j in range(length))
            most = max(most, full * pre[length] + best)

    print(most)

main()
