"""Ticket Price"""

age = int(input())
role = input().lower()

if age < 18 or role == "s":
    print("20")
else:
    print("50")
