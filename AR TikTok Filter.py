"""AR TikTok Filter"""

from math import sqrt

r, x, y = map(float, input().split())
d = sqrt((x ** 2) + (y ** 2))

if d == r:
    print("ON")
elif d < r:
    print("IN")
else:
    print("OUT")
