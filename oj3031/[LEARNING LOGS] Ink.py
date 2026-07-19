"""[LEARNING LOGS] Ink"""

from math import ceil

time = []
spread_rate, amount = map(int, input().split())

for i in range(amount):
    x, y = map(int, input().split())
    area = 3.1416 * (x**2 + y**2)
    method = ceil(area / spread_rate)
    time.append(method)

for i in time:
    print(i)
