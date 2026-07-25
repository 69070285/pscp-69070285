"""Pod"""

data = []
min_row = 2e9
amount, row = map(int, input().split())

for i in range(amount):
    user_row = int(input())
    data.append(user_row)

for i in range(1, row + 1):
    if data.count(i) < min_row:
        min_row = data.count(i)

waiting = amount - (min_row * row)
print(waiting)
