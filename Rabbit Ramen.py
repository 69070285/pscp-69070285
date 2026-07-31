"""Rabbit Ramen"""

size, taste = input().split()
add = 0
match size:
    case "S":
        total = 60
    case "M":
        total = 80
    case _:
        total = 100
topping = input()

if taste == "T":
    total += 20

if not topping == "N":
    topping, amount = topping.split()
    if topping == "P":
        add = 15 * int(amount)
    else:
        add = 10 * int(amount)

print(total + add)
