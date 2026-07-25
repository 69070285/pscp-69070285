"""Coke"""

count = 0
total = 0
normal_price = int(input())
promo = int(input())
new_price = int(input())
amount = int(input())

for i in range(1, amount + 1):
    if i > 0:
        if count == promo and promo:
            total += new_price
            count = 0
        else:
            total += normal_price
        count += 1

print(total)
