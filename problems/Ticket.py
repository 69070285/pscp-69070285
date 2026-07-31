"""Ticket"""

age, day = input().split()
price = 0

if int(age) >= 19:
    price = 150
elif 5 <= int(age) <= 18:
    price = 100

match day:
    case "Wed":
        print(f"{price / 2:.0f}")
    case _:
        print(price)
