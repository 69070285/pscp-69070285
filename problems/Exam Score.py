"""Exam Score"""

amount = int(input())
all_scores = []

for i in range(amount):
    if i >= 0:
        score = int(input())
        all_scores.append(score)

print(max(all_scores))
print(all_scores.count(max(all_scores)))
