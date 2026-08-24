"""Inflation"""

def main():
    """Main Function"""
    price = int(float(input()) * 100)
    time = int(input())

    for _ in range(time):
        price += (price * 381) // 10000

    print(f"{price // 100}.{price % 100:02d}")

main()
