"""Heads and Legs"""

def main():
    """Main Function"""
    head, leg = int(input()), int(input())
    rab = (leg - 2 * head) // 2
    print(f"{rab} {head - rab}" if not leg % 2 and 2 * head <= leg <= 4 * head else "Impossible")

main()
