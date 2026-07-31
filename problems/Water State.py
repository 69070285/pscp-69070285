"""Water State"""

degree = int(input())
unit = input().lower()

if unit == "f":
    degree = (degree - 32) * (5 / 9)

if degree <= 0:
    print("solid")
elif degree >= 100:
    print("gas")
else:
    print("liquid")
