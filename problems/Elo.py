"""Elo"""

result = 0
ra = int(input())
rb = int(input())
method = input().upper().strip()

if method == "A":
    result = 1 / (1 + 10 ** ((rb - ra) / 400.0))
elif method == "B":
    result = 1 / (1 + 10 ** ((ra - rb) / 400.0))

print(f"{result:.2f}")
