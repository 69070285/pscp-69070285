"""Pass or Not Pass"""

mid_score = int(input())
final_score = int(input())
total = mid_score + final_score

print(total)
if total >= 50:
    print("pass")
else:
    print("fail")
