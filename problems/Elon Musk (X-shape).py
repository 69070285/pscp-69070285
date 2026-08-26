"""Elon Musk (X-shape)"""

def main():
    """Main Function"""
    amount, sign = input().split()
    amount = int(amount)
    center = amount // 2

    for i in range(amount):
        row = []
        for j in range(amount):
            if i == j or i + j == amount - 1:
                if sign == "#":
                    row.append("#")
                else:
                    dist = abs(i - center)
                    row.append(chr(ord(sign) + dist))
            else:
                row.append("-")
        print("".join(row))

main()
