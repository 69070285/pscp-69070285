"""RectangleArea"""

x1, y1, width1, height1 = map(int, input().split())
x2, y2, width2, height2 = map(int, input().split())

top = min(y1 + height1, y2 + height2)
bottom = max(y1, y2)
right = min(x1 + width1, x2 + width2)
left = max(x1, x2)

if top <= bottom or right <= left:
    print("no overlapping")
else:
    print((top - bottom) * (right - left))
