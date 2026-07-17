"""Milk"""

price = float(input())
cap = int(input())
claim = int(input())
money = float(input())
total = 0
result = 0
add = 0

while money >= price:
    total += 1
    money -= price

if not cap:
    print(total)
else:
    result = total
    while total >= cap:
        add = (total // cap) * claim
        result += add
        total = (total % cap) + add

    print(result)
