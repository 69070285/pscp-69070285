"""Calculator"""

result = 0
number = int(input())

if number == 1:
    print("1")
else:
    for i in range(1, number + 1):
        result += len(str(i)) + 1
    print(result)
