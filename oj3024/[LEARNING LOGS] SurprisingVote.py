"""[LEARNING LOGS] SurprisingVote"""

total_score = float(input())
max_score = float(input())
min_score = total_score - (max_score * 2)
if min_score < 0:
    min_score = total_score - (max_score * (total_score // max_score))

if max_score - min_score > 2 or max_score > total_score:
    print("Surprising")
elif (not max_score and total_score) or (max_score * 3  < total_score):
    print("Surprising")
else:
    print("Not surprising")
