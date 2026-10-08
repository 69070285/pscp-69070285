"""Coke V2"""

def main():
    """Main Function"""
    normal = int(input())
    promo = int(input())
    cheap = int(input())
    amount = int(input())

    if not promo or not amount:
        print(amount * normal)
    else:
        trade = (amount - 1) // promo
        print((amount - trade) * normal + trade * cheap)

main()
