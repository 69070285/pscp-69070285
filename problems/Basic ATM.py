"""Basic ATM"""

money = int(input())

if 100 <= money <= 20000 and not money % 100:
    if money >= 1000:
        print(f"1000 = {money // 1000}")
        money %= 1000
    if money >= 500:
        print(f"500 = {money // 500}")
        money %= 500
    if money >= 100:
        print(f"100 = {money // 100}")
        money %= 100
else:
    print("ERROR")
