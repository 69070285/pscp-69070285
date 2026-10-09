"""ProgressiveTax_Midterm2014"""

def main():
    """Main Function"""
    money = int(input())
    tax = 0
    calculate = [
        (4000000, 0.35), (2000000, 0.30), (1000000, 0.25),
        (750000, 0.20), (500000, 0.15), (300000, 0.10), (150000, 0.05)
    ]

    for limit, rate in calculate:
        if money > limit:
            tax += (money - limit) * rate
            money = limit

    print(int(tax))

main()
