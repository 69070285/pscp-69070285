"""[MIDTERM] RealThaiPlus"""

def main():
    """Main Function"""
    wallet = int(input())
    day = int(input())
    success = 0
    permonth = 1000

    for _ in range(day):
        if permonth < 200:
            perday = permonth
        else:
            perday = 200
        item_amount = int(input())

        for _ in range(item_amount):
            price = int(input()) * 100
            pay = int(price * 0.4)
            tht = (int(price * 0.6) + (pay % 100)) // 100
            if tht > 200:
                pay = (pay // 100) + (tht - perday)
                tht = perday
            else:
                pay //= 100

            if wallet >= 
            

main()
