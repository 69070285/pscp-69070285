"""Meteorite"""

def main():
    """Main Function"""
    weight = float(input())
    extra = int(input())
    target = float(input())
    attack, amount = 0, 1

    while weight >= target:
        attack += amount
        amount *= weight / (weight / extra)
        weight /= extra

    print(int(attack))

main()
