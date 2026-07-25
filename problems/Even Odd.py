"""Even Odd"""

odd = 0
even = 0

for i in range(3):
    if i >= 0:
        number = int(input())
        if not number % 2:
            even += 1
        else:
            odd += 1

print(even)
print(odd)
