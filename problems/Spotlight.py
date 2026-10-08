"""Spotlight"""

def main():
    """Main Function"""
    amount = int(input())
    spot = []
    for _ in range(amount):
        s, e = map(int, input().split())
        if e < s:
            e += 360
        spot.append((s, e))
        spot.append((s + 360, e + 360))
    spot.sort()

    best = 0
    cur_s, cur_e = spot[0]
    for s, e in spot[1:]:
        if s <= cur_e:
            cur_e = max(cur_e, e)
        else:
            best = max(best, cur_e - cur_s)
            cur_s, cur_e = s, e

    best = max(best, cur_e - cur_s)
    print(min(best, 360))

main()
