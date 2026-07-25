"""[LEARNING LOGS] BrickBridge"""

small_brick = int(input())
large_brick = int(input())
target = int(input())
total_brick = 0
out_of_brick = False

while target:
    if not (small_brick + large_brick):
        out_of_brick = True
        break

    if (target >= 5) and (not large_brick):
        target -= 5
        large_brick -= 1
    elif (target >= 1) and (not small_brick):
        target -= 1
        small_brick -= 1

    total_brick += 1

if out_of_brick:
    print("-1")
else:
    print(total_brick)
