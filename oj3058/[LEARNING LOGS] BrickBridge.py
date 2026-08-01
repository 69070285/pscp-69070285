"""[LEARNING LOGS] BrickBridge"""

small_brick = int(input())
large_brick = int(input())
target = int(input())
large_brick = min(target // 5, large_brick)
target = target - large_brick * 5

if small_brick >= target:
    print(target)
else:
    print("-1")
