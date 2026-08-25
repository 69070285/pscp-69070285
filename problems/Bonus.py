"""Bonus"""

data = input().split()
role = data[0]
exp = int(data[1])
earn = int(data[2])

if role == "M":
    if exp <= 5:
        print(int(earn * 0.06 + 1500))
    elif 5 < exp <= 10:
        print(int(earn * 0.08 + 1500))
    else:
        print(int(earn * 0.1 + 1500))
elif role == "B":
    if exp <= 5:
        print(int(earn * 0.05 + 1000))
    elif 5 < exp <= 10:
        print(int(earn * 0.06 + 1000))
    else:
        print(int(earn * 0.07 + 1000))
else:
    if exp <= 5:
        print(int(earn * 0.04 + 500))
    elif 5 < exp <= 10:
        print(int(earn * 0.05 + 500))
    else:
        print(int(earn * 0.06 + 500))
