"""Grocery"""

carrot, cabbage, tomato = map(int, input().split())
carrot = carrot * 10
cabbage = cabbage * 25
tomato = tomato * 3
total = carrot + cabbage + tomato

print(total)
