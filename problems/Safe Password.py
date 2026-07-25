"""Safe Password"""

username = input()
password = input()

if username != "H" and password != "4567":
    print("safe locked")
elif username != "H":
    print("safe locked - change char")
elif password != "4567":
    print("safe locked - change digit")
else:
    print("safe unlocked")
