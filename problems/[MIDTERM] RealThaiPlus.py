"""[MIDTERM] RealThaiPlus"""

def main():
    """Main Function"""
    wallet = int(input())
    day = int(input())
    permonth = 1000

    for _ in range(day):
        perday = 200
        item_amount = int(input())
        for _ in range(item_amount):
            price = int(input())

main()
