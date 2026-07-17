"""[LEARNING LOGS] Divide 10"""

number = int(input())
number = number - (number % 10)
result = []

for i in range(number, -1, -10):
    result.append(i)

print(" ".join(map(str, result)))
