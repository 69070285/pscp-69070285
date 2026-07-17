"""Milk"""

price = float(input())
cap = int(input())
claim = int(input())
money = float(input())
total = 0

while money >= price:
    total += 1
    money -= price

if not cap:
    print(total)
else:
    total = total + ((total // cap) * claim)
    print(total)
