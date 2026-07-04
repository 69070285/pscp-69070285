"""[LEARNING LOGS] Bill"""

price = int(input())
service = price * 0.1
if service <= 50:
    service = 50
elif service >= 1000:
    service = 1000

price += service
total = price + price * 0.07
print(format(total, ".2f"))
