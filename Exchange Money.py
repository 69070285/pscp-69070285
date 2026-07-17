"""Exchange Money"""

money = float(input())

ten_baht = money // 10
money = money % 10
five_baht = money // 5
money = money % 5
two_baht = money // 2
money = money % 2
one_baht = money // 1
money = money % 1

print(f"10 = {int(ten_baht)}")
print(f"5 = {int(five_baht)}")
print(f"2 = {int(two_baht)}")
print(f"1 = {int(one_baht)}")
