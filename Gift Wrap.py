"""Gift Wrap"""

radius, height, add = map(float, input().split())
long = (2 * 3.14 * radius) + add
width = (radius * 2) + height

print(f"{width:.2f} {long:.2f}")
