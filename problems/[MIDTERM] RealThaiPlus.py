"""[MIDTERM] RealThaiPlus"""

def main():
    """Main Function"""
    wallet = int(input())
    day_count = int(input())
    per_month = 1000
    success = 0

    for _ in range(day_count):
        per_day = 200
        amount = int(input())

        for _ in range(amount):
            price = int(input())
            self = (price * 40) // 100
            tht = price - self

            if tht > per_day:
                tht = per_day
            if tht > per_month:
                tht = per_month

            pay = price - tht
            if wallet >= pay:
                wallet -= pay
                per_day -= tht
                per_month -= tht
                success += 1

    print(success)
    print(wallet)
    print(1000 - per_month)

main()
