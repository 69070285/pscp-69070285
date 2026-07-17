"""Min Number OG"""

check = 2e9

for i in range(3):
    if i >= 0:
        number = int(input())
        if number < check:
            check = number

print(check)
