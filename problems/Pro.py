"""Pro"""

come = int(input())
pay = int(input())
price = int(input())
amount = int(input())
amount = amount - (amount // come) * (come - pay)

print(amount * price)
