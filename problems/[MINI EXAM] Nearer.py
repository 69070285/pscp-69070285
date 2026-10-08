"""[MINI EXAM] Nearer"""

def main():
    """Main Function"""
    alice = int(input())
    bob = int(input())
    icecream = int(input())
    alice = abs(icecream - alice)
    bob = abs(icecream - bob)

    if alice < bob:
        print(f"Alice {alice}")
    elif alice > bob:
        print(f"Bob {bob}")
    else:
        print(f"Sundaes {alice}")

main()
