"""Distance 3D"""

from math import sqrt

x1, y1, z1 = map(int, input().split())
x2, y2, z2 = map(int, input().split())

distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
print(format(distance, ".2f"))
