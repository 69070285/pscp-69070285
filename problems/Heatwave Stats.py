"""Heatwave Stats"""

def main():
    """Main Function"""
    amount = int(input())
    stats = sorted(list(map(float, input().split())))

    print(f"SUM={sum(stats):.2f}")
    print(f"AVG={sum(stats) / amount:.2f}")
    if amount % 2:
        print(f"MEDIAN={stats[amount // 2]:.2f}")
    else:
        print(f"MEDIAN={(stats[amount // 2 - 1] + stats[amount // 2]) / 2:.2f}")
    print(f"MAX={max(stats):.2f}")
    print(f"MIN={min(stats):.2f}")
    print(f"ALERT={sum(1 for s in stats if s >= 37)}")
    print(f"SORTED={" ".join(f"{s:.2f}" for s in stats)}")

main()
