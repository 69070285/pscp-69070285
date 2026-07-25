"""[LEARNING LOGS] Mod Range"""

start = int(input())
stop = int(input())
divisor = int(input())
remainder = int(input())
result = 0

for i in range(start, stop + 1):
    if i % divisor == remainder:
        result += 1

print(result)
