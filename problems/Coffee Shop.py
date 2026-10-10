"""Coffee Shop"""

def main():
    """Main Function"""
    price, b, c, d = float(input()), float(input()), float(input()), float(input())
    amount = int(input())
    promo1 = price + (amount - 1) * (1 - b / 100) * price
    promo2 = price * amount * (1 - c / 100) if price * amount >= d else price * amount

    print("1" if promo1 < promo2 else "2")
    print(f"{min(promo1, promo2):.2f}")

main()
