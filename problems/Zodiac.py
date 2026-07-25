"""Zodiac"""

day = int(input())
month = int(input())

if (day >= 22 and month == 12) or (day <= 19 and month == 1):
    print("capricorn")
elif (day >= 20 and month == 1) or (day <= 18 and month == 2):
    print("aquarius")
elif (day >= 19 and month == 2) or (day <= 20 and month == 3):
    print("pisces")
elif (day >= 21 and month == 3) or (day <= 19 and month == 4):
    print("aries")
elif (day >= 20 and month == 4) or (day <= 20 and month == 5):
    print("taurus")
elif (day >= 21 and month == 5) or (day <= 19 and month == 6):
    print("gemini")

if (day >= 22 and month == 6) or (day <= 22 and month == 7):
    print("cancer")
elif (day >= 23 and month == 7) or (day <= 22 and month == 8):
    print("leo")
elif (day >= 23 and month == 8) or (day <= 22 and month == 9):
    print("virgo")
elif (day >= 23 and month == 9) or (day <= 23 and month == 10):
    print("libra")
elif (day >= 24 and month == 10) or (day <= 21 and month == 11):
    print("scorpio")
elif (day >= 22 and month == 11) or (day <= 21 and month == 12):
    print("sagittarius")
