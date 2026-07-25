"""Leap Year"""

year = int(input())

if not year % 4:
    if (not year % 100 and year >= 1582) or year == 1500:
        if not year % 400 or year == 1500:
            print("yes")
        else:
            print("no")
    else:
        print("yes")
else:
    print("no")
