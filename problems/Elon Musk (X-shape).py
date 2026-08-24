"""Elon Musk (X-shape)"""

def main():
    """Main Function"""
    amount, sign = input().split()
    amount = int(amount)
    base = ord('A') if sign.isupper() else ord('a')

    for i in range(1, amount + 1):
        for j in range(1, amount + 1):
            if sign == "#":
                if i == j or i + j == amount + 1:
                    print("#", end="")
                else:
                    print("-", end="")
            else:
                if i == j or i + j == amount + 1:
                    distance = min(i - 1, amount - i)
                    offset = (amount // 2) - distance
                    print(chr(base + (ord(sign) - base + offset) % 26), end="")
                else:
                    print("-", end="")
        print()

main()
