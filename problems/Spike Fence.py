"""Spike Fence"""

width, height, floor = map(int, input().split())
price = int(input())
width *= 2
height *= 2
sum_lenght = (width + height) * floor

print(sum_lenght)
print(sum_lenght * price)
