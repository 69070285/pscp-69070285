"""Vowel Amount"""

result = 0
amount = int(input())

for i in range(amount):
    if i >= 0:
        letter = input()
        if letter in ("A", "E", "I", "O", "U"):
            result += 1

print(result)
