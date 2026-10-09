"""RuleofThree"""

def main():
    """Main Function"""
    best_price, best_product = 1, -1

    for _ in range(int(input())):
        price, product = float(input()), float(input())
        worth, best_worth = product /  price, best_product / best_price
        if (worth > best_worth) or (worth == best_worth and price < best_price):
            best_price = price
            best_product = product

    print(f"{best_price:.2f} {best_product:.2f}")

main()
