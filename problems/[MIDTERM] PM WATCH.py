"""[MIDTERM] PM WATCH"""

def main():
    """Main Function"""
    amount = int(input())
    over = 0
    peak = 0
    streak = 0
    most_streak = 0
    start = 0
    cur_start = 0

    for i in range(1, amount + 1):
        pm = int(input())
        if pm > peak:
            peak = pm
        if pm > 50:
            over += 1
            if not streak:
                cur_start = i
            streak += 1
            if streak >= most_streak:
                most_streak = streak
                start = cur_start
        else:
            streak = 0

    print(f"OVER = {over}")
    print(f"PEAK = {peak}")
    print(f"STREAK = {most_streak}")
    print(f"START = {start if over > 0 else 0}")

main()
