"""Collect Magic Coins"""

def main():
    """Main Function"""
    fire = 0
    water = 0
    earth = 0
    amount = int(input())

    for _ in range(amount):
        data = list(map(int, input().split()))
        data = sorted([data[:3], data[3:]], key=lambda d: d[0] + d[1] + d[2])
        fire += data[-1][0]
        water += data[-1][1]
        earth += data[-1][2]

    print(f"Total: {fire + water + earth}")
    print(f"Fire: {fire}")
    print(f"Water: {water}")
    print(f"Earth: {earth}")
    print("Bonus: YES" if fire > water + earth else "Bonus: NO")

main()
