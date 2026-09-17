"""Overtake"""

def main():
    """Main Function"""
    amount, lap = map(int, input().split())
    runner = [int(input()) for _ in range(amount)]
    fastest = min(runner)
    count = sum(1 for s in runner if s == fastest or s * (lap - 1) < lap * fastest)
    print(count)

main()
